# Planificateur de tour (`bot/`)

Notes de conception issues du sparring ; le code fait foi pour les détails. Objectif : un algo qui sort une
suite d'actions (déplacements, armes, puces, cibles) en lisant le loadout, pilotable par quelques poids, et
qui tient dans `cœurs × 1 M` opérations sans jamais retomber sur un plan par défaut.

## Pourquoi pas un arbre de combos

Le modèle de coût interdit de déléguer au moteur : `weaponCell` = 38 k ops, `weaponCells` = 26 k, `useWeapon`
= 3 k, chaque lecture de propriété 5–15. Un BFS maison sur les 613 cases coûte ~15 k. Donc : **un snapshot en
début de tour, tout le raisonnement en Python pur, l'API touchée seulement pour exécuter** (`world.py`,
`executor.py`). Bonus : le planificateur se teste en `pytest` sur des grilles ASCII (`uvx pytest tests`).

Un tour Leek Wars a une structure qui rend la recherche de séquences inutile :
- l'ordre des actions à une même case est fixe (entraves → dégâts → poison → soins/boucliers) ;
- les PT sont un sac à dos (coût, usages max, cooldown), pas une séquence ;
- la position ne compte qu'aux **arrêts** (cases d'où on agit) et à la case finale.

## Pipeline

```
world.snapshot()   API → World (grille au tour 1, entités, stats, skills avec cooldown)
skills             item.features → Skill(kind, coût, portée, lancer, LOS, usages, valeur)
danger.Danger      danger(c) = Σ_e dmg_e[dist_e[c]]  — O(1) par case, ~20 k ops par ennemi et par état
planner.Planner    contextes × arrêts × sac à dos × variantes × repli, anytime sur System.operations
executor.execute   rejoue le plan, vérifie les retours
```

**Skills.** Deux familles. *Additives* (dégâts, poison, soin, boucliers) : valeur en PV, optimisées par le
sac à dos « une option par skill » (`group_knapsack`), un skill utilisé à un seul arrêt. *Structurelles* :
+PM/+PT/+force sur moi = **contextes** (un `Ent` dérivé chacun) ; entrave PM/PT sur un ennemi = **variante**
(sa map de danger change, on évalue avec et sans) ; téléportation = **arête** dans le graphe des arrêts
(9 PT, 0 PM, une fois par tour, aussi utilisable en repli).

**Map de danger.** Pour chaque ennemi et chaque état (base, PM entravés, PT entravés) : BFS de sa zone
atteignable, champ de distance (sans obstacles) depuis cette zone, `dmg_e[d]` = meilleure dépense de PT avec
ses skills de portée ≥ d. Pessimiste : LOS ennemie et portée min ignorées, cooldowns ennemis non lus, LINE
approximé en cercle. Les états sont cachés et combinés à la demande (`Danger.combined`).

**Arrêts.** Générés depuis les cibles : pattern de portée de chaque skill offensif autour de chaque ennemi,
filtré par « atteignable à pied » (`reach0`) ou « par téléportation » (rayon 12 depuis ma case), classé par
`borne sup − w_safety × danger`, K meilleurs par ennemi (`k_walk`, `k_tp`), LOS vérifiée sur ceux-là seulement.
Le premier arrêt est toujours la case de départ (agir avant de bouger est permis).

**Recherche.** Beam sur les séquences d'arrêts (`max_stops`, `beam`), BFS paresseux depuis un arrêt non
final, borne sup lâche (`bound`) contre le meilleur score, coupure dès que `System.operations` dépasse
`budget × maxOperations`. Le plan « rester + agir » existe dès la première évaluation.

**Score.** Monnaie unique, le PV :
`value − w_safety × danger(fin) + w_pressure × pression(fin) + w_kill × kills − w_tp_reserve × téléport + engage(fin) × gain_futur`.
Un soin vaut les PV rendus, un poison ses tours décotés, une entrave `danger_avant − danger_après`
(implicitement, via la variante). `w_low_life` favorise les cibles blessées.

**Contre la passivité (horizon d'un tour).** Sans ces termes, s'éloigner coûte 0 et un buff inutilisé ce
tour vaut 0 : l'IA fuit jusqu'à se faire engager.
- *Pression* `pression(c)` = ce que je pourrais infliger au prochain tour depuis c (PM/PT max) ; le repli
  minimise `w_safety × danger − w_pressure × pression` et, à égalité en zone sûre, se rapproche du bord de
  la zone ennemie (en zone dangereuse : s'en éloigne).
- *Engagement* `engage(c) ∈ [0, 1]` = 1 si un ennemi peut m'atteindre depuis c (map de danger, ou
  téléportation + mobilité + portée — la téléportation adverse n'entre pas dans la map, sinon tout est
  rouge), sinon `pression(c) / mon alpha`.
- *Exposition* = `max(danger(fin), engage(fin) × alpha ennemi)` : c'est contre elle que les boucliers sont
  valorisés (`% × exposition`, + un peu pour leurs tours suivants), en 2e passe du sac à dos une fois la
  case finale connue. Les buffs multi-tours (protéine) gagnent `engage(fin) × Δalpha × tours futurs décotés`.
- Projections ennemies sur PT/PM **max** + bottes (ils se rechargent à son tour).

**Skills sur soi (2e passe du sac à dos, case finale connue).** Boucliers à *rendement décroissant* : triés
par absorption, le k-ième ne réduit que ce qui reste après les k−1 meilleurs (relatif en %, absolu par coup
× 3), et prend `w_stack^(k−1)` pour en garder pour les tours suivants (cooldowns désynchronisés). Buffs de
caractéristique (force, magie, agilité, sagesse, résistance, science, puissance ; RAW ou amplifiés par la
science) : celui qui synergise le mieux avec les attaques du tour est un *contexte* (effet exact), les
autres sont des options valant `engage(fin) × Δalpha × tours futurs décotés` — Wizardry passe avant un
troisième mur quand on joue poison.

**Létal.** `lethal_check` : dégâts attendus sur la case finale × Π(1 − relatifs posés ce tour) − absolus ×
coups, comparés à `lethal_margin × PV après soins`. Létal → `− w_death`. Si des boucliers/soins peuvent
l'éviter, *passe de survie* : ils sont revalorisés avec un crédit `w_death / exposition` par PV absorbé et le
sac à dos est relancé ; on garde la meilleure des deux allocations (score avec malus). Le raffinement LOS
refait le test (une cachette lève le malus). Côté offensif, un kill vaut `w_kill + alpha(e) × tours futurs`.

**Alliés.** Les skills de support (soin, boucliers, buffs de stat) forment un groupe par skill dont les
options sont « sur moi » (case finale connue) et « sur l'allié a depuis l'arrêt i » (portée + LOS, masque de
cibles `Effect.Target.*` lu sur l'effet). Valeur sur un allié : ses PV manquants, `Danger.danger_vs(a)`
(champs de distance ennemis réutilisés, sac à dos de dégâts recalculé contre SES boucliers), ou
`engage × Δalpha(a)`, × `w_ally` × `ally_weights[nom]`, avec crédit `w_death` s'il peut mourir. Les cases
d'où un support atteint un allié sont des arrêts candidats (`waypoints`), au même titre que les cases de
tir. *Menace d'équipe* `threat(e)` = max(alpha de e sur moi, alpha sur chaque allié × son poids) : c'est elle
qui pondère le bonus de kill et la priorisation. Une entrave ou un kill rapporte aussi `w_safety × Σ_a w_a ×
(danger_vs(a) avant − après)` : le danger retiré aux alliés compte comme le mien. Pas encore : position pour
couper une LOS ennemie vers un allié.

**Canal (`team.py`).** Après son tour, chaque leek publie (`executor.announce`, `Network.sendAll`, type
CUSTOM, JSON `{t, f, e}`) sa cible principale et s'il a *engagé* (un kill, ou un plan valant ≥ `engage_share`
de son alpha). Au snapshot, les rapports des alliés (≤ 1 tour) donnent `team.focus` (× `w_team_focus`) et
`team.engaged` → `engage() = 1` partout : le combat est lancé, on se buffe et on presse. Qui engage en
premier : le premier dans l'ordre de jeu dont le planner trouve une frappe qui vaut le coup — typiquement
la téléportation vers une cible commode, que le score trouve seul. Les poisons ne passent pas par le canal :
`Ent.poison_load` (Σ valeur × tours des poisons actifs, lu sur `enemy.effects`) décote un poison
supplémentaire (× `w_poison_overflow`) au-delà de `poison_cap` × PV de la cible — un antidote effacerait tout.

**Priorisation de cible** (`target_weights`, une fois par tour) : la valeur des dégâts sur `e` est
multipliée par `(1 + w_threat × alpha(e)/alpha max) × w_summon si invocation × w_finish si vie ≤ mon alpha
× w_focus si cible principale du tour précédent`, puis par `(1 + w_low_life × (1 − vie/max))`. La cible
principale est mémorisée dans `planner.focus` (globale : survit au tour).

**Cachettes.** `w_cover` (PV par obstacle à distance ≤ 2) oriente le repli vers les cases adossées à un
obstacle. Puis, sur les `refine_plans` meilleurs plans, `Danger.refined()` recalcule le danger de la case
finale et de `refine_cells` cases couvertes atteignables avec la **vraie LOS** depuis toutes les cases que
chaque ennemi peut atteindre (≤ `refine_los` appels `lineOfSight` par case, sinon pessimiste). Si aucune
ne voit la cachette, le danger réel tombe à 0 : « tirer puis se cacher » gagne sans règle spéciale
(~130 appels LOS ≈ 4 k ops par tour mesurés).

## Budget mesuré (proxy : lignes Python exécutées, grille 625 cases, 1 ennemi, 9 skills)

`max_stops=1` : ~100 k lignes ; `max_stops=2` : ~120 k, 34 évaluations. Le moteur compte aussi les
expressions : compter ×2–3 en ops réelles. Postes principaux : sac à dos (~900 lignes / évaluation),
champ de distance (~17 k / ennemi / état), BFS (~3–15 k chacun). `Phases` affiche la ventilation par tour
en `debug=True`.

## Hors périmètre v1 (à ajouter dans l'ordre)

1. Zones d'effet (viser une case vide pour toucher sans LOS) : un objectif `AoE(e)` dont les cases cibles
   sont le rayon d'aire autour de l'ennemi ; `effectiveArea` (78 ops) seulement sur le top-K.
2. Répartition d'un skill sur plusieurs arrêts (pistolet 2× ici, 2× là).
3. Types de lancer LINE/DIAGONAL dans la map de danger (la LOS est faite, sur les finalistes).
4. Invocations (cf ci-dessous), grappin/gant de boxe (déplacent l'ennemi = contexte), position pour couper
   une LOS vers un allié.

## Invocations : comment ça rentrerait

- **Le bulbe joue avec le même planner.** Pendant son tour, `Fight.me` EST le bulbe : `snapshot()` lit ses
  puces (`bulbChips`) et ses stats, `Planner` planifie, `execute` agit. Le callback passé à `me.summon` est
  donc `turn()` avec un `Profile` léger. Contrainte forte : **le tour du bulbe consomme MON budget d'ops**
  (même compteur, cf runtime.md) → `max_stops=1`, `refine_plans=0`, `budget` réduit pour lui.
- **Décider d'invoquer** = un skill structurel `SUMMON` (effet 14), comme un buff : valeur = contribution
  attendue du bulbe (`alpha_of` d'un `Ent` fabriqué depuis `bulbStats` + `bulbChips`, ou capacité de soin)
  × tours futurs décotés, moins son coût en PT ; contexte « avec invocation » évalué comme les autres.
- **Où le poser** : mini-objectif sur les cases à portée de la puce — pour un bulbe de dégâts,
  `pression(c) − danger(c)` calculés avec SES portées ; pour un soigneur, près des alliés (danger_vs).
- Une fois posé, c'est un allié (`summoned=True`) : `ally_weights` (0.3 pour un bulbe), support, menace
  d'équipe. Limites : `SUMMON_LIMIT = 8`, `summon` = 1 750 ops, cooldown de la puce.
