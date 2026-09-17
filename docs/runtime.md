# Python sur Leek Wars : modèle d'exécution et pièges

Notes de sparring, tirées du **runtime réel** (`vendor/generator/objects.py`, `PolyglotEntityAI.java`,
`PolyglotSandbox.java` du dépôt `leek-wars/leek-wars-generator`) et du guide de portage interne
(`vendor/generator/POLYGLOT_PORTING_GUIDE.md`). L'article joueur est dans `python_encyclopedia.md`,
la référence membre par membre dans `api_reference.md`.

## 1. Cycle de vie d'une IA

- Moteur : **GraalPy, Python 3.12** dans une sandbox GraalVM (`sandbox.MaxHeapMemory`, threads, AST depth, etc.).
- **Tour 1** : le fichier d'entrée est évalué une fois. S'il définit `turn()`, elle est appelée ; sinon
  le top-level EST la logique de tour et **le source entier est ré-évalué à chaque tour** (`context.eval(source)`,
  donc les globales sont réinitialisées : pas de mémoire entre tours sans `turn()`).
- **Tours suivants** : `turn()` rejouée ; les globales / attributs de classe persistent. Rien n'est réinitialisé,
  y compris tes listes — pense au `clear()`.
- **Hooks** (depuis 09/2026) : `beforeFight()` (avant le tour 1 ; sert surtout à `Fight.me.setLoadout(nom)`,
  le budget ops/RAM est recalculé après) et `afterFight()` (`Fight.winner`). Conditions : une IA **avec `turn()`**
  dont le top-level n'agit pas ; sinon le chargement spéculatif est jeté et le hook silencieusement ignoré.
- `Fight.me` est un singleton **inscriptible** (tu peux ranger ton état dessus : `Fight.me.plan = ...`), et son `id`
  est dynamique : pendant le tour d'un bulbe invoqué via `me.summon(chip, cell, callback)`, `Fight.me` EST le bulbe.
  Tous les autres objets de l'API sont **en lecture seule** (`AttributeError` si tu écris `cell.x = 3`).
- Une erreur non rattrapée dans `turn()` interrompt le tour (les actions déjà faites restent) ; au tour 1 un
  échec de setup ferme le contexte et l'IA repart de zéro au tour suivant.

## 2. Ce qui est exposé, et comment

- Les noms publics (`Fight`, `Field`, `Entity`, `Cell`, `Weapon`, `Chip`, `Effect`, `Feature`, `Message`, `Me`, `Leek`,
  `Turret`, `Bulb`, `Chest`, `Mob`, `Plant`, `State`, `Registers`, `Network`, `Debug`, `System`, `Color`, `Math`)
  sont posés sur `builtins` : visibles **sans import, y compris dans tes modules importés**.
- Il n'y a **ni fonctions plates ni constantes plates** (`getNearestEnemy()`, `WEAPON_PISTOL` : `NameError`).
  Pas de global `me` : `Fight.me`.
- Les entités, cellules, armes, puces sont **poolées** : `me.weapon is Weapon.pistol`, `path[0] is me.cell`,
  `effect.item is Chip.toxin` marchent. Les types sont réels : `isinstance(e, Bulb)`, `isinstance(e, Mob)`.
- `Effect` / `Feature` / `Message` enveloppent des tableaux bruts (`.raw`). Effet ACTIF (`entity.effects`) ≠
  caractéristique déclarée d'un item (`chip.features` : `minValue`/`maxValue`/`turns`/`targets`).
- Constantes : instances camelCase (`Weapon.pistol`, `Chip.bandage`) ; catégories en MAJUSCULES
  (`Effect.DAMAGE`, `State.UNHEALABLE`, `Entity.Stat.STRENGTH`, `Entity.Type.LEEK`, `Cell.Type.EMPTY`,
  `Item.Area.CIRCLE_1`, `Item.LaunchType.LINE`, `Fight.Type.SOLO`, `Fight.Context.GARDEN`, `Fight.Use.SUCCESS`,
  `Effect.Modifier.STACKABLE`, `Effect.Target.ENEMIES`, `Field.NEXUS`, `Color.RED`). Pas de `PI`, `SORT_*`,
  `TYPE_*` : c'est du Python (`math.pi`, `sorted`, `type()`).
- Valeurs de retour des actions : `Fight.Use.SUCCESS = 1`, `CRITICAL = 2`, tout échec `<= 0`
  (`NOT_ENOUGH_TP`, `INVALID_POSITION`, `INVALID_TARGET`, `MAX_USES`, `INVALID_COOLDOWN`, `TOO_MANY_SUMMONS`...).
  Test idiomatique : `if me.useWeapon(enemy) > 0`.
- **Nullabilité** : le stub dit `-> Entity` / `-> Cell`, mais le runtime renvoie `None` quand il n'y a rien
  (`getNearestEnemy()`, `weaponCell()`, `cellFromXY()` hors carte, `cell.entity`, `entity.weapon`, `effect.caster`...).
  C'est voulu côté éditeur (éviter des faux positifs Pyright) : garde tes `if x is None`.
- Arguments souples : partout où l'API attend une cellule / entité / arme / puce, elle accepte **l'objet ou son id**
  (`CellLike = Cell | Entity | int` : passer une entité là où on attend une cellule = sa cellule).
- Helpers de ciblage (`weaponCell(s)`, `chipCell(s)`, `weaponTargets`, `chipTargets`) vivent sur `Fight` et sont
  aliasés sur `me` ; cible d'abord, arme optionnelle ensuite (ordre inverse toléré). Cible entité OU cellule
  (routage automatique vers `getCellToUseWeapon` / `...OnCell`). L'arme par défaut = celle équipée.
- `print()` est redirigé vers le journal de combat (`Debug.log`), avec ses limites anti-spam.
- Registres : `Registers.get/set/delete/all` — clés ≤ 100 caractères, valeurs ≤ 5000, 100 registres max ;
  tout est **str** (sérialise en JSON toi-même).

## 3. Budget d'exécution (le vrai enjeu pour les algos)

- **Opérations** : `maxOperations = cœurs × 1 000 000` par tour (`EntityAI.applyEntityBudgets`). Dépasser jette
  `TOO_MUCH_OPERATIONS` : le tour est coupé.
- En Python, le compteur est un **instrument Truffle** qui compte statements + expressions (patch GraalPy) avec un
  facteur de calibration **×1.0** vs LeekScript (JS : ×0.6). Les préludes du moteur ne sont pas comptés. Certains
  natifs sont facturés au tarif LeekScript (`math.sqrt`, `math.cos`, `random.random`, `pow`, `bin`, `hex`...),
  les fonctions de combat facturent leur coût hôte (ex. `getNearestEnemy` 25 ops, `getPath` beaucoup plus) —
  le coût de chaque membre est indiqué dans la docstring du stub (« — N opérations »).
- `System.operations` est lisible à tout moment (chemin guest rapide) : **borne tes recherches** avec
  `if System.operations > System.maxOperations * 0.8: break`. C'est le piège n°1 du guide de portage : une IA
  de recherche qui ne se borne pas explore tout, tombe sur le **watchdog wall-clock de 5 s/tour**, et après
  **3 dépassements l'IA est neutralisée pour le combat**.
- Un `__lw_pending` de facturation différée existe : la lecture est légèrement en retard sur la réalité, garde une marge.
- **RAM** : cap = `min(50, RAM) × 8 Mo / 3.8` (facteur de parité JS/Py vs LeekScript) **+ 128 Mo de baseline**
  pour le runtime Python lui-même (`POLYGLOT_PYTHON_MIN_HEAP_MB`). Dépasser = `OUT_OF_MEMORY`, contexte fermé,
  et **IA désactivée pour tout le combat** dans le chemin classique — évite les tables géantes construites au tour 1.
- **Wall-clock** : 5 s par tour (backstop), même compteur pour le callback d'un bulbe.
- `MAX_TURNS = 64`, `SUMMON_LIMIT = 8`, `CRITICAL_FACTOR` (cf constantes dans le stub).

## 4. Déterminisme et sandbox

- `random` est seedé par la graine du combat ; `random.seed()` sans argument, `os.urandom`, `SystemRandom`,
  `uuid4` sont reroutés vers le PRNG seedé ; `time` / `datetime` figés. Les combats sont rejouables, ton IA aussi.
- Stdlib disponible (`math`, `itertools`, `collections`, `heapq`, `functools`, `bisect`, `dataclasses`, `json`,
  `re`, `random`...), **pas de pip**, pas de fichiers / réseau / process / threads. `math.cbrt` et `math.exp2`
  sont shimés (manquants dans GraalPy).
- Multi-fichiers : `import` natif, montage en mémoire de tes fichiers (en fin de `sys.path`, la stdlib prime).
  Noms de modules sans tirets, pas d'imports circulaires, chaque `import` d'un voisin exécute son top-level.

## 5. Divergences Python vs LeekScript (si tu portes du code ou lis des IA LS)

| Cas | LeekScript | Python |
|---|---|---|
| `null` dans une somme | vaut 0 | `TypeError` → `(f() or 0)` |
| Index hors bornes / clé absente | `null` | `IndexError` / `KeyError` → `.get()` |
| Division entière | `\` | `int(a / b)` (pas `//` avec des négatifs : arrondi différent) |
| `/ 0` | `null` | `ZeroDivisionError` |
| `for v in map` | valeurs | clés |
| `round(2.5)` | 3 | **2** (arrondi bancaire) — assumé par le moteur, pas masqué |
| Bitmask 64 bits | natif | `int` illimité, OK |
| Retour implicite | `null` | `None` |
| `"" + n` | coerce | `str(n)` / f-string |
| Callback avec args en trop | ignorés | `TypeError` |

## 6. Coût typique des appels de combat (pour raisonner sur un algo)

Chaque accès à une propriété (`e.life`, `c.x`) est un **appel hôte** facturé au tarif LeekScript de la fonction
plate correspondante (`getLife` ...) : mets en cache ce que tu relis dans une boucle (`hp = e.life` avant le `for`).
Les plus chers sont les recherches de chemin et de cases (`path`, `pathLength`, `weaponCells`, `chipCells`,
`effectiveArea`) ; regarde « — N opérations » dans le survol de chaque membre.

## 7. Où vérifier une intuition

- Comportement exact d'une méthode : `vendor/generator/objects.py` (≈ 900 lignes, lisible ; ex. `_weaponCall` pour
  l'ordre des arguments, `_ent` pour le typage des entités).
- Signature exacte vue par l'éditeur : `data/leekwars_raw.pyi` (régénéré par `tools/fetch_sources.sh`).
- Doc officielle FR d'une fonction : `data/function_doc.fr.json` (avec exemples Python pour 62 fonctions) ; lien
  `https://leekwars.com/help/documentation/<fonction LeekScript>` dans chaque docstring.
- Le dépôt public `leek-wars/leek-wars` (client) est **en retard** sur le bundle déployé ; le stub est donc
  extrait du bundle de prod. `leek-wars-generator` (moteur), lui, est à jour (`objects.py` pushé la veille de ces notes).
