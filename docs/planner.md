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
3. Checks létaux : « je peux le tuer ce tour → `w_safety = 0` », « il peut me tuer depuis c → danger ∞ ».
4. Types de lancer LINE/DIAGONAL dans la map de danger (la LOS est faite, sur les finalistes).
5. Alliés (objectif `Protect`, `w_ally`), invocations, grappin/gant de boxe (déplacent l'ennemi = contexte).
