# Référence de l'API objet Python Leek Wars

Générée par `tools/gen_stub.py` (game data `9cee98e38aec8265`). Signatures = stub exact de l'éditeur ; docs = documentation FR officielle de la fonction LeekScript équivalente. Voir aussi `docs/runtime.md`.

## Fight

### `Fight.me: Me`

VOTRE entité (remplace l'ancien global `me`). Pendant le tour d'un bulbe invoqué, `Fight.me` EST le bulbe.

Renvoie votre entité.

**Retour**
- **entity** : Votre entité.

LeekScript : `getEntity()` — 5 opérations · https://leekwars.com/help/documentation/getEntity

### `Fight.turn: int`

Renvoie le tour actuel du combat. 
Le nombre de tours maximum est `MAX_TURNS`.

*Exemple* : se booster au tour 2 :
```python
if Fight.turn == 2:
	Fight.me.useChip(Chip.motivation)
	Fight.me.useChip(Chip.protein)
```

**Retour**
- **turn** : Le tour actuel du combat.

LeekScript : `getTurn()` — 15 opérations · https://leekwars.com/help/documentation/getTurn

### `Fight.id: int`

Retourne l'id du combat actuel.

**Retour**
- **id** : L'id du combat actuel.

LeekScript : `getFightID()` — 5 opérations · https://leekwars.com/help/documentation/getFightID

### `Fight.type: int`

Retourne le type de combat actuel.

**Retour**
- **fightType** : Selon le type de combat :
	- Combat en solo (`FIGHT_TYPE_SOLO`)
	- Combat d'éleveur (`FIGHT_TYPE_FARMER`)
	- Combat d'équipe (`FIGHT_TYPE_TEAM`)
	- Battle Royale (`FIGHT_TYPE_BATTLE_ROYALE`)
	- Combat de boss (`FIGHT_TYPE_BOSS`)

LeekScript : `getFightType()` — 10 opérations · https://leekwars.com/help/documentation/getFightType

### `Fight.context: int`

Retourne le contexte du combat actuel.

**Retour**
- **context** : Selon le contexte du combat :
	- Combat de test (`FIGHT_CONTEXT_TEST`)
	- Combat en arène (`FIGHT_CONTEXT_GARDEN`)
	- Combat en tournoi (`FIGHT_CONTEXT_TOURNAMENT`)
	- Combat en défi (`FIGHT_CONTEXT_CHALLENGE`)

LeekScript : `getFightContext()` — 10 opérations · https://leekwars.com/help/documentation/getFightContext

### `Fight.batched: bool`

Détermine si le combat a été lancé dans un **lot** de combats, et non un par un. Un combat de lot a le même type et le même contexte qu'un combat lancé seul : c'est la seule façon de les distinguer. Sert par exemple à se taire (les logs coûtent des opérations) quand on mesure son IA sur une série de combats.

**Retour**
- **batch** : vrai si le combat fait partie d'un lot, faux s'il a été lancé seul.

LeekScript : `isBatchFight()` — 10 opérations · https://leekwars.com/help/documentation/isBatchFight

### `Fight.boss: int`

Retourne le boss (`Les Boss`) du combat actuel.
Retourne `0` si le combat n'est pas un combat de boss. (cf. `getFightType`)

**Paramètres**
- **boss** : Selon le boss :
	- Nasu Samouraï (`BOSS_NASU_SAMURAI`)
	- Roi Fenouil (`BOSS_FENNEL_KING`)
	- Potiron Maléfique (`BOSS_EVIL_PUMPKIN`)

LeekScript : `getFightBoss()` — 10 opérations · https://leekwars.com/help/documentation/getFightBoss

### `Fight.winner: int`

Retourne le côté de l'équipe gagnante. À utiliser uniquement dans **afterFight()** (voir `Hooks de combat`). Renvoie `-1` si le combat n'est pas terminé.

**Retour**
- **winner** : Le côté gagnant : 0 (notre côté), 1 (côté adverse), 2 (égalité), ou -1 si combat en cours.

LeekScript : `getWinner()` — 5 opérations · https://leekwars.com/help/documentation/getWinner

### `Fight.alliesLife: int`

Retourne la vie totale de vos alliés.

**Retour**
- **life** : La vie totale de vos alliés.

LeekScript : `getAlliesLife()` — 50 opérations · https://leekwars.com/help/documentation/getAlliesLife

### `Fight.enemiesLife: int`

Calcule la somme des points de vie de tous les entités ennemies.

**Retour**
- **life** : La somme des points de vie de l'équipe ennemie.

LeekScript : `getEnemiesLife()` — 50 opérations · https://leekwars.com/help/documentation/getEnemiesLife

### `Fight.getNearestEnemy() -> Entity`

Renvoie l'entité ennemie la plus proche de votre entité.

**Retour**
- **nearestEnemy** : L'entité ennemie la plus proche.
    - `-1` si vous n'avez pas d'ennemi

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getNearestEnemy()` — 25 opérations · https://leekwars.com/help/documentation/getNearestEnemy

### `Fight.getNearestAlly() -> Entity`

Renvoie l'entité alliée la plus proche de votre entité.

**Retour**
- **nearestAlly** : L'entité alliée la plus proche.
     - `-1` si vous n'avez pas d'allié

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getNearestAlly()` — 25 opérations · https://leekwars.com/help/documentation/getNearestAlly

### `Fight.getFarthestEnemy() -> Entity`

Détermine l'ennemi le plus éloigné de votre entité, à vol d'oiseau.

**Retour**
- **farthestEnemy** : L'entité ennemie la plus éloignée.
	- `-1` si vous n'avez pas d'ennemi

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getFarthestEnemy()` — 31 opérations · https://leekwars.com/help/documentation/getFarthestEnemy

### `Fight.getFarthestAlly() -> Entity`

Détermine l'allié le plus éloigné de votre entité, à vol d'oiseau.

**Retour**
- **farthestAlly** : L'entité alliée la plus éloignée.
	- `-1` si vous n'avez pas d'allié

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getFarthestAlly()` — 31 opérations · https://leekwars.com/help/documentation/getFarthestAlly

### `Fight.getNearestEnemyTo(target: EntityLike) -> Entity`

Renvoie l'entité ennemie la plus proche de l'entité fourni en paramètre.

**Paramètres**
- **entity** : L'id de l'entité dont on veut connaitre l'ennemi le plus proche.

**Retour**
- **enemy** : L'entité ennemie la plus proche.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getNearestEnemyTo()` — 35 opérations · https://leekwars.com/help/documentation/getNearestEnemyTo

### `Fight.getNearestAllyTo(target: EntityLike) -> Entity`

Renvoie l'entité alliée la plus proche de l'entité fourni en paramètre.

**Paramètres**
- **entity** : L'id de l'entité dont on veut connaitre l'allié le plus proche.

**Retour**
- **ally** : L'entité alliée la plus proche.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getNearestAllyTo()` — 35 opérations · https://leekwars.com/help/documentation/getNearestAllyTo

### `Fight.getEnemies() -> list[Entity]`

Renvoie les entités ennemies (vivantes ou mortes) dans le combat.

**Retour**
- **enemies** : Un tableau contenant toutes les entités ennemies.

LeekScript : `getEnemies()` — 100 opérations · https://leekwars.com/help/documentation/getEnemies

### `Fight.getAllies() -> list[Entity]`

Retourne un tableau contenant vos alliés, et votre entité.

**Retour**
- **allies** : Le tableau des alliés et votre entité.

LeekScript : `getAllies()` — 100 opérations · https://leekwars.com/help/documentation/getAllies

### `Fight.getAliveEnemies() -> list[Entity]`

Retourne un tableau de tous vos ennemis vivants dans le combat.

**Retour**
- **enemies** : Un tableau contenant tous vos ennemis vivants.

LeekScript : `getAliveEnemies()` — 100 opérations · https://leekwars.com/help/documentation/getAliveEnemies

### `Fight.getAliveAllies() -> list[Entity]`

Retourne un tableau de tous vos alliés vivants dans le combat.

**Retour**
- **allies** : Un tableau contenant tous vos alliés vivants.

LeekScript : `getAliveAllies()` — 100 opérations · https://leekwars.com/help/documentation/getAliveAllies

### `Fight.getDeadEnemies() -> list[Entity]`

Renvoie les entités ennemies mortes.

**Retour**
- **deadEnemies** : Le tableau des entités ennemies mortes.

LeekScript : `getDeadEnemies()` — 100 opérations · https://leekwars.com/help/documentation/getDeadEnemies

### `Fight.getDeadAllies() -> list[Entity]`

Renvoie les entités alliées mortes.

**Retour**
- **deadAllies** : Le tableau des entités alliées mortes.

LeekScript : `getDeadAllies()` — 100 opérations · https://leekwars.com/help/documentation/getDeadAllies

### `Fight.getEnemiesCount() -> int`

Renvoie le nombre d'ennemis (morts ou vivants) dans le combat.

**Retour**
- **numEnemies** : Le nombre d'ennemis.

LeekScript : `getEnemiesCount()` — 25 opérations · https://leekwars.com/help/documentation/getEnemiesCount

### `Fight.getAlliesCount() -> int`

Renvoie le nombre d'alliés (morts ou vivants) dans le combat.

**Retour**
- **numAllies** : Le nombre d'alliés.

LeekScript : `getAlliesCount()` — 25 opérations · https://leekwars.com/help/documentation/getAlliesCount

### `Fight.getAliveEnemiesCount() -> int`

Renvoie le nombre d'ennemis vivants dans le combat.

**Retour**
- **numAliveEnemies** : Le nombre d'ennemis vivants.

LeekScript : `getAliveEnemiesCount()` — 25 opérations · https://leekwars.com/help/documentation/getAliveEnemiesCount

### `Fight.getAliveAlliesCount() -> int`

Renvoie le nombre d'alliés en vie dans le combat (entité appelante incluse).

Voir aussi `getAliveAllies` et `getAlliesCount`.

**Retour**
- **allies** : Le nombre d'alliés en vie.

LeekScript : `getAliveAlliesCount()` — 100 opérations · https://leekwars.com/help/documentation/getAliveAlliesCount

### `Fight.getDeadEnemiesCount() -> int`

Renvoie le nombre d'ennemis morts dans le combat.

**Retour**
- **numDeadEnemies** : Le nombre d'ennemis morts.

LeekScript : `getDeadEnemiesCount()` — 25 opérations · https://leekwars.com/help/documentation/getDeadEnemiesCount

### `Fight.getAlliedTurret() -> Entity`

Retourne la tourelle de votre équipe ou `null` si elle n'existe pas.

**Retour**
- **alliedTurret** : La tourelle de votre équipe.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getAlliedTurret()` — 15 opérations · https://leekwars.com/help/documentation/getAlliedTurret

### `Fight.getEnemyTurret() -> Entity`

Retourne la tourelle ennemie ou `null` si elle n'existe pas.

**Retour**
- **enemyTurret** : La tourelle ennemie.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getEnemyTurret()` — 15 opérations · https://leekwars.com/help/documentation/getEnemyTurret

### `Fight.getNearestEnemyToCell(cell: CellLike) -> Entity`

Renvoie l'entité ennemie la plus proche de la cellule fournie en paramètre.

**Paramètres**
- **cell** : L'id de la cellule dont on veut connaitre l'ennemi le plus proche.

**Retour**
- **enemy** : L'entité ennemie la plus proche.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getNearestEnemyToCell()` — 35 opérations · https://leekwars.com/help/documentation/getNearestEnemyToCell

### `Fight.getNearestAllyToCell(cell: CellLike) -> Entity`

Renvoie l'entité alliée la plus proche de la cellule fournie en paramètre.

**Paramètres**
- **cell** : L'id de la cellule dont on veut connaitre l'allié le plus proche.

**Retour**
- **ally** : L'entité alliée la plus proche.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getNearestAllyToCell()` — 35 opérations · https://leekwars.com/help/documentation/getNearestAllyToCell

### `Fight.getNextPlayer(entity: EntityLike = ...) -> Entity`

Renvoie l'entité qui jouera après l'entité **entity**. Sans paramètre, renvoie l'entité qui jouera après l'entité **entity**, ou l'entité actuelle par défaut.

**Paramètres**
- **entity** : L'id de l'entité de référence.

**Retour**
- **player** : Le joueur suivant.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getNextPlayer()` — 20 opérations · https://leekwars.com/help/documentation/getNextPlayer

### `Fight.getPreviousPlayer(entity: EntityLike = ...) -> Entity`

Renvoie l'entité ayant joué avant l'entité **entity**. Sans paramètre, renvoie l'entité ayant joué avant le joueur actuel.

**Paramètres**
- **entity** : L'id de l'entité de référence.

**Retour**
- **player** : Le joueur précédent.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getPreviousPlayer()` — 20 opérations · https://leekwars.com/help/documentation/getPreviousPlayer

### `Fight.listen() -> list`

Renvoie le tableau des say() des entités précédentes, sous la forme [entity_id, message].

**Retour**
- **messages** : Le tableau des say() précédents.

LeekScript : `listen()` — 78 opérations · https://leekwars.com/help/documentation/listen

### `Fight.weaponCell(target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> Cell`

Renvoie une cellule où votre entité pourra utiliser l'arme **weapon** sur l'entité **entity**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

Exemple pour utiliser le `Laser` :
```python
cell = Fight.me.weaponCell(enemy, Weapon.laser)
Fight.me.moveToward(cell)
Fight.me.useWeapon(enemy)
```

**Paramètres**
- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

**Retour**
- **cell** : La cellule d'où l'arme pourra être utilisée.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getCellToUseWeapon()` — 38080 opérations · https://leekwars.com/help/documentation/getCellToUseWeapon

### `Fight.weaponCells(target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> list[Cell]`

Retourne la liste des cellules à partir desquelles votre entité pourra utiliser l'arme **weapon** sur l'entité **entity**.
Attention, la cellule du lanceur fera partie du résultat si l'arme a un effet sur le lanceur, comme le `J-Laser` par exemple.

**Paramètres**
- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

**Retour**
- **cells** : Liste des cellules d'où l'arme pourra être utilisée.

LeekScript : `getCellsToUseWeapon()` — 25834 opérations · https://leekwars.com/help/documentation/getCellsToUseWeapon

### `Fight.chipCell(chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> Cell`

Renvoie une cellule où votre entité pourra utiliser la puce **chip** sur l'entité **entity**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

Exemple pour lancer un `Rocher` :
```python
cell = Fight.me.chipCell(Chip.rock, enemy)
Fight.me.moveToward(cell)
Fight.me.useChip(Chip.rock, enemy)
```

**Paramètres**
- **chip** : La puce que l'entité veut pouvoir utiliser.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut un tableau vide.

**Retour**
- **cell** : La cellule d'où la puce pourra être utilisée.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getCellToUseChip()` — 38080 opérations · https://leekwars.com/help/documentation/getCellToUseChip

### `Fight.chipCells(chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> list[Cell]`

Retourne la liste des cellules à partir desquelles votre entité pourra utiliser la puce **chip** sur l'entité **entity**.

**Paramètres**
- **chip** : La puce que l'entité veut pouvoir utiliser.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

**Retour**
- **cells** : Liste des cellules d'où la puce pourra être utilisée.

LeekScript : `getCellsToUseChip()` — 25834 opérations · https://leekwars.com/help/documentation/getCellsToUseChip

### `Fight.weaponTargets(cell: CellLike, weapon: WeaponLike = ...) -> list[Entity]`

Renvoie les entités qui seront affectées si l'arme **weapon** est utilisée sur la cellule **cell**.
Attention, le lanceur fera partie du résultat si l'arme a un effet sur son lanceur, comme le `J-Laser` par exemple.

**Paramètres**
- **weapon** : L'arme à tester.
- **cell** : La cellule cible.

**Retour**
- **targets** : Le tableau contenant toutes les entités qui seront affectées.

LeekScript : `getWeaponTargets()` — 40 opérations · https://leekwars.com/help/documentation/getWeaponTargets

### `Fight.chipTargets(chip: ChipLike, cell: CellLike) -> list[Entity]`

Renvoie les entités qui seront affectées si la puce **chip** est utilisée sur la cellule **cell**.

**Paramètres**
- **chip** : La puce à tester.
- **cell** : La cellule cible.

**Retour**
- **targets** : Le tableau contenant toutes les entités qui seront affectées.

LeekScript : `getChipTargets()` — 40 opérations · https://leekwars.com/help/documentation/getChipTargets

### `Fight.CRITICAL_FACTOR: int`

(= 1.3)

LeekScript : `CRITICAL_FACTOR`

### `Fight.MAX_TURNS: int`

(= 64) Nombre de tours maximum dans un combat.

LeekScript : `MAX_TURNS`

### `Fight.SUMMON_LIMIT: int`

(= 8)

LeekScript : `SUMMON_LIMIT`

## Me

### `Me.moveToward(target: CellLike, mp: int = ...) -> int`

Rapproche votre entité d'une autre entité **entity**, en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **entity** : L'entité vers lequelle votre entité doit se rapprocher.
- **mp** : Le nombre maximum de PM à utiliser.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveToward()` — 500 opérations · https://leekwars.com/help/documentation/moveToward

### `Me.moveAwayFrom(target: CellLike, mp: int = ...) -> int`

Éloigne votre entité d'un autre entité **entity**, en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **entity** : L'entité dont votre entité doit s'éloigner.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveAwayFrom()` — 500 opérations · https://leekwars.com/help/documentation/moveAwayFrom

### `Me.moveTowardCells(cells: list, mp: int = ...) -> int`

Rapproche votre entité de la première cellule d'un ensemble de cellules **cells**, en utilisant au maximum **mp** points de mouvement.

Si, parmi l'ensemble de cellules **cells**, il y a une cellule à portée de déplacement et qui rapproche votre entité de la première cellule de **cells**, alors l'entité va se déplacer sur la cellule de **cells** la plus proche de la case de départ de l'entité.

Si, parmi l'ensemble de cellules **cells**, il n'y a aucune cellule à portée de déplacement et qui rapproche votre entité de la première cellule de **cells**, alors l'entité va se rapprocher de la première cellule de l'ensemble de cellules **cells** en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **cells** : Le tableau contenant la cellule vers laquelle votre entité doit se rapprocher, et les cellules sur lesquelles votre entité va se déplacer si elles sont à portée.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveTowardCells()` — 500 opérations · https://leekwars.com/help/documentation/moveTowardCells

### `Me.moveTowardEntities(entities: list, mp: int = ...) -> int`

Rapproche votre entité d'un ensemble d'entités **entities**, en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **entities** : Le tableau contenant les ids des entités vers lesquelles votre entité doit se rapprocher.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveTowardEntities()` — 500 opérations · https://leekwars.com/help/documentation/moveTowardEntities

### `Me.moveTowardLine(a: CellLike, b: CellLike, mp: int = ...) -> int`

Rapproche votre entité d'une ligne définie par deux cellules **cell1** et **cell2**, en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **cell1** : La cellule 1.
- **cell2** : La cellule 2.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveTowardLine()` — 500 opérations · https://leekwars.com/help/documentation/moveTowardLine

### `Me.moveAwayFromCells(cells: list, mp: int = ...) -> int`

Éloigne votre entité d'un ensemble de cellules **cells**, en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **cells** : Le tableau contenant les cellules dont votre entité doit s'éloigner.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveAwayFromCells()` — 500 opérations · https://leekwars.com/help/documentation/moveAwayFromCells

### `Me.moveAwayFromEntities(entities: list, mp: int = ...) -> int`

Éloigne votre entité d'un ensemble de entités **entities**, en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **entities** : Le tableau contenant les ids des entités dont votre entité doit s'éloigner.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveAwayFromEntities()` — 500 opérations · https://leekwars.com/help/documentation/moveAwayFromEntities

### `Me.moveAwayFromLine(a: CellLike, b: CellLike, mp: int = ...) -> int`

Éloigne votre entité d'une ligne définie par deux cellules **cell1** et **cell2**, en utilisant au maximum **mp** points de mouvement.

**Paramètres**
- **cell1** : La cellule 1.
- **cell2** : La cellule 2.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

**Retour**
- **mp** : Le nombre de points de mouvements utilisés.

LeekScript : `moveAwayFromLine()` — 500 opérations · https://leekwars.com/help/documentation/moveAwayFromLine

### `Me.useWeapon(target: EntityLike) -> int`

Utilise l'arme sélectionnée sur l'entité **entity**.

*Exemple* : utiliser le pistolet sur l'ennemi le plus proche :
```python
enemy = Fight.getNearestEnemy()
Fight.me.setWeapon(Weapon.pistol)
Fight.me.useWeapon(enemy)
```

**Paramètres**
- **entity** : Entité ciblée.

**Retour**
- **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useWeapon sont :
	- `USE_CRITICAL`, en cas de coup critique
	- `USE_SUCCESS`, en cas de réussite
	- `USE_FAILED`, en cas de d'échec
	- `USE_INVALID_TARGET`, si la cible n'existe pas
	- `USE_NOT_ENOUGH_TP`, si votre entité n'a pas assez de TP
	- `USE_INVALID_POSITION`, si la portée est mauvaise ou la ligne de vue n'est pas dégagée
	- `USE_MAX_USES`, si l'arme a déjà été utilisée trop de fois dans le tour.

Les valeurs `USE_SUCCESS` et `USE_CRITICAL` valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de l'arme a réussi en effectuant le test :
```python
if Fight.me.useWeapon(entity) > 0:
	# L'utilisation a réussi !
else:
	# L'utilisation a échoué !
```

LeekScript : `useWeapon()` — 3000 opérations · https://leekwars.com/help/documentation/useWeapon

### `Me.useWeaponOnCell(cell: CellLike) -> int`

Utilise l'arme sélectionnée sur la cellule **cell**.

*Exemple* : utiliser le pistolet sur l'ennemi le plus proche :
```python
enemyCell = Fight.getNearestEnemy().cell
Fight.me.setWeapon(Weapon.pistol)
Fight.me.useWeaponOnCell(enemyCell)
```

**Paramètres**
- **cell** : Cellule ciblée.

**Retour**
- **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useWeapon sont :
	- `USE_CRITICAL`, en cas de coup critique
	- `USE_SUCCESS`, en cas de réussite
	- `USE_FAILED`, en cas de d'échec
	- `USE_INVALID_TARGET`, si la cible n'existe pas
	- `USE_NOT_ENOUGH_TP`, si votre entité n'a pas assez de TP
	- `USE_INVALID_POSITION`, si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs `USE_SUCCESS` et `USE_CRITICAL` valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de l'arme a réussi en effectuant le test :
```python
if Fight.me.useWeaponOnCell(cell) > 0:
	# L'utilisation a réussi !
else:
	# L'utilisation a échoué !
```

LeekScript : `useWeaponOnCell()` — 3000 opérations · https://leekwars.com/help/documentation/useWeaponOnCell

### `Me.useChip(chip: ChipLike, target: EntityLike = ...) -> int`

Utilise la puce **chip** sur l'entité **entity**, ou sur vous-même si le second paramètre n'est pas fourni.

*Exemple* : Utiliser la puce `Motivation` sur moi-même :
```python
Fight.me.useChip(Chip.motivation)
```
*Exemple* : Utiliser la puce `Décharge` sur un enemi :
```python
Fight.me.useChip(Chip.shock, enemy)
```

**Paramètres**
- **chip** : Chip à utiliser.
- **entity** : Entité cible, par défaut votre entité.

**Retour**
- **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useChip sont :
	- `USE_CRITICAL`, en cas de coup critique
	- `USE_SUCCESS`, en cas de réussite
	- `USE_FAILED`, en cas de d'échec
	- `USE_INVALID_TARGET`, si la cible n'existe pas
	- `USE_NOT_ENOUGH_TP`, si votre entité n'a pas assez de TP
	- `USE_INVALID_COOLDOWN`, si la puce n'est pas encore utilisable
	- `USE_INVALID_POSITION`, si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs `USE_SUCCESS` et `USE_CRITICAL` valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de la puce a réussi en effectuant le test :
```python
if Fight.me.useChip(chip, entity) > 0:
	# L'utilisation a réussi !
else:
	# L'utilisation a échoué !
```

LeekScript : `useChip()` — 3000 opérations · https://leekwars.com/help/documentation/useChip

### `Me.useChipOnCell(chip: ChipLike, cell: CellLike) -> int`

Utilise la puce **chip** sur la cellule **cell**.

**Paramètres**
- **chip** : Chip à utiliser.
- **cell** : Cellule cible.

**Retour**
- **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useChipOnCell sont :
	- `USE_CRITICAL`, en cas de coup critique
	- `USE_SUCCESS`, en cas de réussite
	- `USE_FAILED`, en cas de d'échec
	- `USE_INVALID_TARGET`, si la cible n'existe pas
	- `USE_NOT_ENOUGH_TP`, si votre entité n'a pas assez de TP
	- `USE_INVALID_COOLDOWN`, si la puce n'est pas encore utilisable
	- `USE_INVALID_POSITION`, si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs `USE_SUCCESS` et `USE_CRITICAL` valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de la puce a réussi en effectuant le test :
```python
if Fight.me.useChipOnCell(chip, cell) > 0:
	# L'utilisation a réussi !
else:
	# L'utilisation a échoué !
```

LeekScript : `useChipOnCell()` — 3000 opérations · https://leekwars.com/help/documentation/useChipOnCell

### `Me.setWeapon(weapon: WeaponLike) -> bool`

Équipe l'arme **weapon** sur votre entité.

Cette fonction coûte **1PT** .

Pour éviter de rééquiper la même arme et de perdre ce PT à chaque tour, il est possible d'utiliser une condition `if` comme ceci :
```python
if Fight.me.weapon != Weapon.pistol:
	Fight.me.setWeapon(Weapon.pistol)
```

**Paramètres**
- **weapon** : Id de l'arme à équiper.

LeekScript : `setWeapon()` — 15 opérations · https://leekwars.com/help/documentation/setWeapon

### `Me.say(message: Any) -> bool`

Fait déclarer la phrase **message** à votre entité.

Cette fonction coûte **1PT** .

La longueur du message est limitée à **100**, le surplus sera coupé.
Pour limiter la surcharge de blabla, une limite de **2** say() par tour est en place.

*Exemple* : saluer son adversaire :
```python
Fight.me.say(f"Salut à toi, {Fight.getNearestEnemy().name} !")
```

**Paramètres**
- **message** : Message qu'annonçera votre entité dans l'arène.

LeekScript : `say()` — 30 opérations · https://leekwars.com/help/documentation/say

### `Me.lama() -> None`

Fait dire « lama » à l'entité (trophée).

LeekScript : `lama()` · https://leekwars.com/help/documentation/lama

### `Me.canUseWeapon(target: EntityLike | WeaponLike, weapon: WeaponLike | EntityLike = ...) -> bool`

Détermine si votre entité peut tirer sur l'entité d'id **entity** avec l'arme **weapon** depuis sa cellule courante.

La fonction vérifie les points suivants :
 - Portée : comparaison entre la distance et la portée minimale et maximale de l'arme.
 - Ligne de vue dégagée entre les deux positions (`lineOfSight`).
 
La fonction ne vérifie pas si vous avez les `PT` suffisants pour le coût de l'arme ou si l'arme est équipée.

**Paramètres**
- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **entity** : L'id de l'entité sur lequel vous voulez tirer.

**Retour**
- **canUse** : `true` si votre entité peut tirer, `false` sinon.

LeekScript : `canUseWeapon()` — 45 opérations · https://leekwars.com/help/documentation/canUseWeapon

### `Me.canUseWeaponOnCell(cell: CellLike | WeaponLike, weapon: WeaponLike | CellLike = ...) -> bool`

Détermine si votre entité peut tirer sur la cellule **cell** avec l'arme **weapon** depuis sa cellule courante.

La fonction vérifie les points suivants :
 - Portée : comparaison entre la distance et la portée minimale et maximale de l'arme.
 - Ligne de vue dégagée entre les deux positions (`lineOfSight`).
 
La fonction ne vérifie pas si vous avez les `PT` suffisants pour le coût de l'arme ou si l'arme est équipée.

**Paramètres**
- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **cell** : Le numéro de la cellule sur laquelle vous voulez tirer.

**Retour**
- **canUse** : `true` si votre entité peut tirer sur la cellule, `false` sinon.

LeekScript : `canUseWeaponOnCell()` — 45 opérations · https://leekwars.com/help/documentation/canUseWeaponOnCell

### `Me.canUseChip(chip: ChipLike, target: EntityLike) -> bool`

Détermine si votre entité peut utiliser la puce **chip** sur l'entité d'id **entity** depuis sa cellule courante.

La fonction vérifie les points suivants :
 - Portée : comparaison entre la distance et la portée minimale et maximale de la puce.
 - Ligne de vue dégagée entre les deux positions (`lineOfSight`).
 
La fonction ne vérifie pas si vous avez les `PT` suffisants pour le coût de la puce ou si la puce n'est pas en récupération (temps de récupération : `getCooldown`).

**Paramètres**
- **chip** : Le numéro de la puce à tester.
- **entity** : L'id de l'entité sur lequel vous voulez utiliser la puce.

**Retour**
- **canUse** : `true` si votre entité peut utiliser la puce, `false` sinon.

LeekScript : `canUseChip()` — 45 opérations · https://leekwars.com/help/documentation/canUseChip

### `Me.canUseChipOnCell(chip: ChipLike, cell: CellLike) -> bool`

Détermine si votre entité peut utiliser la puce **chip** sur la cellule **cell** depuis sa cellule courante.

La fonction vérifie les points suivants :
- Portée : comparaison entre la distance et la portée minimale et maximale de la puce.
- Ligne de vue dégagée entre les deux positions (`lineOfSight`).
 
La fonction ne vérifie pas si vous avez les `PT` suffisants pour le coût de la puce ou si la puce n'est pas en récupération (temps de récupération : `getCooldown`).

**Paramètres**
- **chip** : Le numéro de la puce à tester.
- **cell** : Le numéro de la cellule sur laquelle vous voulez utliser la puce.

**Retour**
- **canUse** : `true` si votre entité peut utiliser la puce, `false` sinon.

LeekScript : `canUseChipOnCell()` — 45 opérations · https://leekwars.com/help/documentation/canUseChipOnCell

### `Me.resurrect(target: EntityLike, cell: CellLike) -> int`

Utilise la puce CHIP_RESURRECTION pour ressusciter une entité d'id **entity** morte, sur la cellule **cell**.

**Paramètres**
- **entity** : L'id de l'entité à faire revivre.
- **cell** : La cellule sur laquelle l'entité réapparaîtra.

**Retour**
- **result** : Le résultat du lancement de la puce, parmi les constantes USE_*.

LeekScript : `resurrect()` — 500 opérations · https://leekwars.com/help/documentation/resurrect

### `Me.itemUses(item: WeaponLike | ChipLike) -> int`

Renvoie le nombre d'utilisations déjà effectuées pendant ce tour d'une arme ou d'une puce .

**Paramètres**
- **item** : un entier désignant l'id de l'arme ou de la puce (ex : WEAPON_PISTOL).

**Retour**
- **uses** : Le nombre d'utilisation effectuées, 0 si l'objet n'a pas encore été utilisé pendant ce tour.

LeekScript : `getItemUses()` — 15 opérations · https://leekwars.com/help/documentation/getItemUses

### `Me.setLoadout(name: str, changeStats: bool = ...) -> bool`

Applique un loadout pour ce combat uniquement, sans modifier l'équipement persistant du poireau. À utiliser uniquement dans **beforeFight()** (voir `Hooks de combat`). Si le nom n'existe pas ou si **setLoadout** est appelé en dehors de **beforeFight()**, la fonction renvoie `false` et un avertissement est ajouté au rapport.

```
// Cette fonction est appelée automatiquement avant le tour 1
function beforeFight() {
	// Choisir un des équipements définis sur la page du poireau
	setLoadout("mon_equipement"); //applique l'équipement "mon_equipement" et consomme une potion de restat si les stats sont différentes
}
```

**Paramètres**
- **name** : Le nom exact du loadout à appliquer (sensible à la casse).

**Retour**
- **success** : `true` si le loadout a été appliqué, `false` sinon.

LeekScript : `setLoadout()` — 100 opérations · https://leekwars.com/help/documentation/setLoadout

### `Me.summon(chip: ChipLike, cell: CellLike, callback: Callable[..., Any], name: str = ...) -> int`

Invoque une entité déterminée par la puce **chip** sur la cellule **cell** ayant pour IA la fonction **ai**.

Vous pouvez retrouver plus d'informations sur la page `Bulbes`.

**Paramètres**
- **chip** : La puce utilisée pour l'invocation. La puce doit être une puce de type invocation et doit être équipée sur l'entité qui utilise la fonction summon.
- **cell** : La cellule ou l'invocation doit apparaître.
- **ai** : L'IA de l'invocation, sous la forme d'une fonction.
- **name** : Le nom personnalisé du bulbe qui sera invoqué.

**Retour**
- **return** : La fonction summon a le même retour que la fonction `useChip`.

LeekScript : `summon()` — 1750 opérations · https://leekwars.com/help/documentation/summon

### `Me.weaponCell(target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> Cell`

Cellule d'où utiliser l'arme (équipée par défaut) sur `target` (entité ou case), ou None. Alias de Fight.weaponCell.

Renvoie une cellule où votre entité pourra utiliser l'arme **weapon** sur l'entité **entity**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

Exemple pour utiliser le `Laser` :
```python
cell = Fight.me.weaponCell(enemy, Weapon.laser)
Fight.me.moveToward(cell)
Fight.me.useWeapon(enemy)
```

**Paramètres**
- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

**Retour**
- **cell** : La cellule d'où l'arme pourra être utilisée.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getCellToUseWeapon()` — 38080 opérations · https://leekwars.com/help/documentation/getCellToUseWeapon

### `Me.weaponCells(target: EntityLike | CellLike, weapon: WeaponLike = ..., ignoredCells: list = ...) -> list[Cell]`

Toutes les cellules d'où utiliser l'arme sur `target`. Alias de Fight.weaponCells.

Retourne la liste des cellules à partir desquelles votre entité pourra utiliser l'arme **weapon** sur l'entité **entity**.
Attention, la cellule du lanceur fera partie du résultat si l'arme a un effet sur le lanceur, comme le `J-Laser` par exemple.

**Paramètres**
- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

**Retour**
- **cells** : Liste des cellules d'où l'arme pourra être utilisée.

LeekScript : `getCellsToUseWeapon()` — 25834 opérations · https://leekwars.com/help/documentation/getCellsToUseWeapon

### `Me.chipCell(chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> Cell`

Cellule d'où utiliser `chip` sur `target`, ou None. Alias de Fight.chipCell.

Renvoie une cellule où votre entité pourra utiliser la puce **chip** sur l'entité **entity**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

Exemple pour lancer un `Rocher` :
```python
cell = Fight.me.chipCell(Chip.rock, enemy)
Fight.me.moveToward(cell)
Fight.me.useChip(Chip.rock, enemy)
```

**Paramètres**
- **chip** : La puce que l'entité veut pouvoir utiliser.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut un tableau vide.

**Retour**
- **cell** : La cellule d'où la puce pourra être utilisée.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getCellToUseChip()` — 38080 opérations · https://leekwars.com/help/documentation/getCellToUseChip

### `Me.chipCells(chip: ChipLike, target: EntityLike | CellLike, ignoredCells: list = ...) -> list[Cell]`

Toutes les cellules d'où utiliser `chip` sur `target`. Alias de Fight.chipCells.

Retourne la liste des cellules à partir desquelles votre entité pourra utiliser la puce **chip** sur l'entité **entity**.

**Paramètres**
- **chip** : La puce que l'entité veut pouvoir utiliser.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

**Retour**
- **cells** : Liste des cellules d'où la puce pourra être utilisée.

LeekScript : `getCellsToUseChip()` — 25834 opérations · https://leekwars.com/help/documentation/getCellsToUseChip

### `Me.weaponTargets(cell: CellLike, weapon: WeaponLike = ...) -> list[Entity]`

Entités touchées si l'arme (équipée par défaut) est lancée sur `cell`. Alias de Fight.weaponTargets.

Renvoie les entités qui seront affectées si l'arme **weapon** est utilisée sur la cellule **cell**.
Attention, le lanceur fera partie du résultat si l'arme a un effet sur son lanceur, comme le `J-Laser` par exemple.

**Paramètres**
- **weapon** : L'arme à tester.
- **cell** : La cellule cible.

**Retour**
- **targets** : Le tableau contenant toutes les entités qui seront affectées.

LeekScript : `getWeaponTargets()` — 40 opérations · https://leekwars.com/help/documentation/getWeaponTargets

### `Me.chipTargets(chip: ChipLike, cell: CellLike) -> list[Entity]`

Entités touchées si `chip` est lancée sur `cell`. Alias de Fight.chipTargets.

Renvoie les entités qui seront affectées si la puce **chip** est utilisée sur la cellule **cell**.

**Paramètres**
- **chip** : La puce à tester.
- **cell** : La cellule cible.

**Retour**
- **targets** : Le tableau contenant toutes les entités qui seront affectées.

LeekScript : `getChipTargets()` — 40 opérations · https://leekwars.com/help/documentation/getChipTargets

## Entity

### `Entity.id: int`

### `Entity.entityType: int`

Genre d'entité (Entity.Type.LEEK / BULB / TURRET / CHEST / MOB / PLANT). Ne pas confondre avec `.type` des sous-classes (Bulb.Type.*, Chest.Type.*...).

Renvoie le type d'entité de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le type sera renvoyé.

**Retour**
- **type** : Le type d'entité de **entity** :
	- [ENTITY_LEEK](https://leekwars.com/help/documentation/ENTITY_LEEK) s'il s'agit d'un poireau.
	- [ENTITY_BULB](https://leekwars.com/help/documentation/ENTITY_BULB) s'il s'agit d'un bulbe.
	- [ENTITY_TURRET](https://leekwars.com/help/documentation/ENTITY_TURRET) s'il s'agit d'une tourelle.
	- [ENTITY_CHEST](https://leekwars.com/help/documentation/ENTITY_CHEST) s'il s'agit d'un coffre.
	- [ENTITY_MOB](https://leekwars.com/help/documentation/ENTITY_MOB) s'il s'agit d'un monstre (en combat de boss).

LeekScript : `getType()` — 15 opérations · https://leekwars.com/help/documentation/getType

### `Entity.life: int`

Renvoie la vie actuelle de l'entité d'id **entity**.
Utilisez `getLife()` sans paramètre pour récupérer votre vie — en JavaScript/TypeScript et en Python, la propriété s'écrit `Fight.me.life`.

Exemple pour se soigner si notre vie est inférieure à 50% :
```python
if Fight.me.life < Fight.me.maxLife * 0.5:  # Si ma vie < 50%
	Fight.me.useChip(Chip.cure)
```

**Paramètres**
- **entity** : L'id de l'entité dont la vie sera renvoyée.

**Retour**
- **life** : La vie actuelle de l'entité **entity**.

LeekScript : `getLife()` — 15 opérations · https://leekwars.com/help/documentation/getLife

### `Entity.maxLife: int`

Renvoie la vie totale de l'entité d'id **entity**. Utilisez `getTotalLife()` sans paramètre pour récupérer votre vie totale.

**Paramètres**
- **entity** : L'id de l'entité dont la vie totale sera retournée.

**Retour**
- **life** : La vie totale de l'entité.

LeekScript : `getTotalLife()` — 15 opérations · https://leekwars.com/help/documentation/getTotalLife

### `Entity.tp: int`

Renvoie le nombre de points de tour de l'entité **entity**. Utilisez `getTP()` sans paramètre pour récupérer vos PT.

**Paramètres**
- **entity** : L'id de l'entité dont les PT seront renvoyés.

**Retour**
- **tp** : Le nombre de PT de l'entité **entity**.

LeekScript : `getTP()` — 15 opérations · https://leekwars.com/help/documentation/getTP

### `Entity.maxTP: int`

Renvoie le nombre maximal de points de tour de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le le nombre maximal de points de tour sera retourné.

**Retour**
- **totalTP** : Le nombre maximal de points de tour de l'entité **entity**.

LeekScript : `getTotalTP()` — 15 opérations · https://leekwars.com/help/documentation/getTotalTP

### `Entity.mp: int`

Revoie le nombre de points de mouvements actuel de l'entité **entity**. Utilisez `getMP()` sans paramètre pour récupérer vos PM.

**Paramètres**
- **entity** : L'id de l'entité dont le nombre de PM sera renvoyé.

**Retour**
- **mp** : Le nombre de PM de l'entité **entity**.

LeekScript : `getMP()` — 15 opérations · https://leekwars.com/help/documentation/getMP

### `Entity.maxMP: int`

Renvoie le nombre maximal de points de mouvement de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le nombre maximal de points de mouvement sera retourné.

**Retour**
- **totalMP** : Le nombre maximal de points de mouvement de l'entité **entity**.

LeekScript : `getTotalMP()` — 15 opérations · https://leekwars.com/help/documentation/getTotalMP

### `Entity.strength: int`

Renvoie la force de l'entité d'id **entity**. Utilisez `getStrength()` sans paramètre pour récupérer votre force.

**Paramètres**
- **entity** : L'entité dont la force sera retournée.

**Retour**
- **strength** : La force de l'entité **entity**.

LeekScript : `getStrength()` — 15 opérations · https://leekwars.com/help/documentation/getStrength

### `Entity.agility: int`

Retourne l'agilité de l'entité d'id **entity**. Pour récupérer directement l'agilité de votre entité, utilisez `getAgility()` sans paramètre.

**Paramètres**
- **entity** : L'id de l'entité dont l'agilité sera retournée.

**Retour**
- **agility** : L'agilité de l'entité **entity**.

LeekScript : `getAgility()` — 15 opérations · https://leekwars.com/help/documentation/getAgility

### `Entity.wisdom: int`

Renvoie la sagesse de l'entité d'id **entity**. Utilisez `getWisdom()` sans paramètre pour récupérer votre sagesse.

**Paramètres**
- **entity** : L'id de l'entité dont la sagesse sera retournée.

**Retour**
- **wisdom** : La sagesse de l'entité d'id **entity**.

LeekScript : `getWisdom()` — 15 opérations · https://leekwars.com/help/documentation/getWisdom

### `Entity.resistance: int`

Renvoie la résistance de l'entité d'id **entity**. Utilisez `getResistance()` sans paramètre pour récupérer votre résistance.

**Paramètres**
- **entity** : L'id de l'entité dont la résistance sera retournée.

**Retour**
- **resistance** : La résistance de l'entité d'id **entity**.

LeekScript : `getResistance()` — 15 opérations · https://leekwars.com/help/documentation/getResistance

### `Entity.science: int`

Renvoie la science de l'entité d'id **entity**. Utilisez `getScience()` sans paramètre pour récupérer votre science.

**Paramètres**
- **entity** : L'id de l'entité dont la science sera retournée.

**Retour**
- **science** : La science de l'entité d'id **entity**.

LeekScript : `getScience()` — 15 opérations · https://leekwars.com/help/documentation/getScience

### `Entity.magic: int`

Renvoie la magie de l'entité d'id **entity**. Utilisez `getMagic()` sans paramètre pour récupérer votre magie.

**Paramètres**
- **entity** : L'id de l'entité dont la magie sera retournée.

**Retour**
- **magic** : La magie de l'entité d'id **entity**.

LeekScript : `getMagic()` — 15 opérations · https://leekwars.com/help/documentation/getMagic

### `Entity.power: int`

Renvoie la puissance de l'entité d'id **entity**.

**Paramètres**
- **entity** : L'entité dont la puissance sera retournée.

**Retour**
- **power** : La puissance de l'entité **entity**.

LeekScript : `getPower()` — 15 opérations · https://leekwars.com/help/documentation/getPower

### `Entity.level: int`

Renvoie le niveau de l'entité d'id **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le niveau sera renvoyé.

**Retour**
- **level** : Le niveau de l'entité d'id **entity**.

LeekScript : `getLevel()` — 15 opérations · https://leekwars.com/help/documentation/getLevel

### `Entity.name: str`

Renvoie le nom de l'entité d'id **entity**.

*Exemple* : saluer l'adversaire :
```python
enemy = Fight.getNearestEnemy()
Fight.me.say(f"Salut {enemy.name} !")
```

**Paramètres**
- **entity** : L'id de l'entité dont le nom sera renvoyé.

**Retour**
- **name** : Le nom de l'entité **entity**.

LeekScript : `getName()` — 15 opérations · https://leekwars.com/help/documentation/getName

### `Entity.absoluteShield: int`

Retourne le bouclier absolu de l'entité d'id **entity**. Pour récupérer directement le bouclier absolu de votre entité, utilisez `getAbsoluteShield()` sans paramètre.

**Paramètres**
- **entity** : L'id de l'entité dont le bouclier absolu sera retourné.

**Retour**
- **shield** : Le bouclier absolu de l'entité **entity**.

LeekScript : `getAbsoluteShield()` — 15 opérations · https://leekwars.com/help/documentation/getAbsoluteShield

### `Entity.relativeShield: int`

Retourne le bouclier relatif de l'entité d'id **entity**. Pour récupérer directement le bouclier relatif de votre entité, utilisez `getRelativeShield()` sans paramètre.

**Paramètres**
- **entity** : L'id de l'entité dont le bouclier relatif sera retourné.

**Retour**
- **shield** : Le bouclier relatif de l'entité **entity**, usuellement un nombre entier entre **0** et **100** (peut techniquement dépasser 100, mais le bouclier relatif maximal effectif est 100%).

LeekScript : `getRelativeShield()` — 15 opérations · https://leekwars.com/help/documentation/getRelativeShield

### `Entity.damageReturn: int`

Retourne le taux de renvoi de dommages de l'entité d'id **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le renvoi de dommages sera retourné.

**Retour**
- **damageReturn** : Le taux de renvoi de dommages de l'entité d'id **entity** (en %).

LeekScript : `getDamageReturn()` — 15 opérations · https://leekwars.com/help/documentation/getDamageReturn

### `Entity.frequency: int`

Renvoie la fréquence de l'entité d'id **entity**. Utilisez `getFrequency()` sans paramètre pour récupérer votre fréquence.

**Paramètres**
- **entity** : L'entité dont la fréquence sera retournée.

**Retour**
- **frequency** : La fréquence de l'entité **entity**.

LeekScript : `getFrequency()` — 15 opérations · https://leekwars.com/help/documentation/getFrequency

### `Entity.cores: int`

Renvoie le nombre de coeurs de l'entité d'id **entity**.

**Paramètres**
- **entity** : L'entité dont le nombre de coeurs sera retournée.

**Retour**
- **cores** : Le nombre de coeurs de l'entité **entity**.

LeekScript : `getCores()` — 15 opérations · https://leekwars.com/help/documentation/getCores

### `Entity.ram: int`

Renvoie la RAM de l'entité **entity**.

**Paramètres**
- **entity** : L'entité dont la RAM sera retournée.

**Retour**
- **ram** : La RAM de l'entité **entity**.

LeekScript : `getRAM()` — 15 opérations · https://leekwars.com/help/documentation/getRAM

### `Entity.cell: Cell`

Retourne la cellule où se trouve l'entité d'id **entity**.
Utilisez `getCell()` sans paramètre pour récupérer votre cellule.

*Exemple* : calculer la distance entre moi et l'enemi, et se booster s'il est proche :
```python
distance = Fight.me.cell.distance(enemy.cell)
if distance < 10:
	Fight.me.useChip(Chip.protein)
```

**Paramètres**
- **entity** : L'id de l'entité dont la cellule sera retournée, par défaut votre entité.

**Retour**
- **cell** : La cellule où se trouve l'entité **entity**.

LeekScript : `getCell()` — 5 opérations · https://leekwars.com/help/documentation/getCell

### `Entity.weapons: list[Weapon]`

Renvoie les armes de l'entité d'id **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont les armes seront renvoyées.

**Retour**
- **weapon** : Un tableau contenant les armes de l'entité **entity**.

LeekScript : `getWeapons()` — 50 opérations · https://leekwars.com/help/documentation/getWeapons

### `Entity.chips: list[Chip]`

Renvoie les puces de l'entité d'id **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont les puces seront renvoyées.

**Retour**
- **chips** : Un tableau contenant les puces de l'entité **entity**.

LeekScript : `getChips()` — 40 opérations · https://leekwars.com/help/documentation/getChips

### `Entity.effects: list[Effect]`

Retourne la liste des effets de l'entité d'id **entity**. Pour récupérer directement la liste des effets de votre entité, utilisez `getEffects` sans paramètre.

**Paramètres**
- **entity** : L'id de l'entité dont la liste des effets sera retourné.

**Retour**
- **effects** : La liste des effets actuellement présents sur l'entité **entity**. La liste des effets est un tableau contenant les effets. Un effet est lui-même un tableau de 8 cases de la forme : 
```
 [type, value, caster_id, turns, critical, item_id, target_id, modifiers]
```
 - **type** est le type de l'effet parmi :
	 - `EFFECT_DAMAGE`, **value** est le nombre de dégâts
	 - `EFFECT_HEAL`, **value** est le nombre de PV soignés
	 - `EFFECT_BUFF_STRENGTH`, **value** est la force gagnée
	 - `EFFECT_BUFF_AGILITY`, **value** est l'agilité gagnée
	 - `EFFECT_BUFF_TP`, **value** est le nombre de PT gagnés
	 - `EFFECT_BUFF_MP`, **value** est le nombre de PM gagnés
	 - `EFFECT_ABSOLUTE_SHIELD`, **value** est le bouclier absolu gagné
	 - `EFFECT_RELATIVE_SHIELD`, **value** est le bouclier relatif gagné
	 - `EFFECT_DEBUFF`, indique un débuff, **value** est le pourcentage d'effets retiré.
etc.
 - *value* : La valeur de l'effet.
 - *caster_id* : L'id de l'entité qui a lancé l'effet.
 - *turns* : Le nombre de tours restants de l'effet.
 - *critical* : Est-ce que l'effet est un coup critique.
 - *item_id* : L'id de l'item qui a provoqué cet effet.
 - *target_id* : L'id de la cible de l'effet (**entity**).
 - *modifiers* : Les modificateurs de l'effet (masque de bits avec les constantes **EFFECT_MODIFIER_***).

**Exemples**
Pour savoir si on est empoisonné :
```python
# affiche une phrase pour chaque effet de poison sur soi
# En API objet les effets sont des OBJETS : effect.type plutôt que effect[0].
for effect in Fight.me.effects:
	if effect.type == Effect.POISON:
		Debug.log(f"Je suis empoisonné de {effect.value} pendant encore {effect.turns} tours")
```

LeekScript : `getEffects()` — 25 opérations · https://leekwars.com/help/documentation/getEffects

### `Entity.launchedEffects: list[Effect]`

Renvoie la liste des effets qu'a provoqué l'entité d'id **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont la liste des effets provoqués sera retournée.

**Retour**
- **effects** : La liste des effets provoqués l'entité d'id **entity**, de la même forme que le tableau renvoyé par `getEffects`.

LeekScript : `getLaunchedEffects()` — 25 opérations · https://leekwars.com/help/documentation/getLaunchedEffects

### `Entity.passiveEffects: list[Feature]`

Retourne la liste des effets passifs de l'entité d'id **entity**. Pour récupérer directement la liste des effets passifs de votre entité, utilisez `getPassiveEffects()` sans paramètre.

**Paramètres**
- **entity** : L'id de l'entité dont la liste des effets passif sera retourné.

**Retour**
- **passiveEffects** : La liste des effets passifs actuellement présents sur l'entité **entity**.
La liste des effets passifs est un tableau contenant les effets. Le retour est le même que pour `getWeaponPassiveEffects`.

LeekScript : `getPassiveEffects()` — 125 opérations · https://leekwars.com/help/documentation/getPassiveEffects

### `Entity.states: list`

Renvoie l'ensemble des états actifs sur l'entité **entity**. Renvoie vos états si le paramètre **entity** n'est pas fourni ou est `null`.

Exemple :
```python
State.INVINCIBLE in entity.states
```

**Paramètres**
- **entity** : L'entité.

**Retour**
- **states** : Un ensemble d'états.

LeekScript : `getStates()` — 25 opérations · https://leekwars.com/help/documentation/getStates

### `Entity.summons: list[Entity]`

Renvoie la liste des invocations actuellement en vie de l'entité d'id **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont les invocations seront renvoyées.

**Retour**
- **summons** : La liste des invocations de l'entité d'id **entity**.

LeekScript : `getSummons()` — 15 opérations · https://leekwars.com/help/documentation/getSummons

### `Entity.summoner: Entity`

Renvoie l'entité qui a invoqué l'entité **entity**, s'il s'agit d'une invocation.

**Paramètres**
- **entity** : L'id de l'entité dont l'invocateur sera renvoyé.

**Retour**
- **summoner** : L'entité qui a invoqué **entity**.
    - `-1` si **entity** n'est pas une invocation
	- `null` si **entity** n'est pas l'identifiant d'une entité du combat

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getSummoner()` — 15 opérations · https://leekwars.com/help/documentation/getSummoner

### `Entity.summoned: bool`

Renvoie si l'entité **entity** est une invocation ou non.

**Paramètres**
- **entity** : L'id de l'entité à tester.

**Retour**
- **summon** : `true` si **entity** est une invocation, `false` sinon.

LeekScript : `isSummon()` — 10 opérations · https://leekwars.com/help/documentation/isSummon

### `Entity.alive: bool`

Détermine si une entité **entity** est vivant. Équivalent à `getLife(entity) > 0`.

**Paramètres**
- **entity** : L'id de l'entité à tester.

**Retour**
- **alive** : `true` si l'entité **entity** est vivant, `false` s'il est mort.

LeekScript : `isAlive()` — 15 opérations · https://leekwars.com/help/documentation/isAlive

### `Entity.dead: bool`

Détermine si l'entité **entity** est mort. Équivalent à `getLife(entity) == 0`.

**Paramètres**
- **entity** : L'id de l'entité à tester.

**Retour**
- **dead** : `true` si l'entité **entity** est mort, `false` s'il est vivant.

LeekScript : `isDead()` — 15 opérations · https://leekwars.com/help/documentation/isDead

### `Entity.isStatic: bool`

Renvoie si l'entité **entity** est statique ou non. Une entité statique ne peut pas se déplacer ou être déplacée.

C'est notamment le cas des `Tourelles` d'équipe.

*Exemple* :
```python
if entity.isStatic:
	Debug.log("Cette entité ne peut pas être déplacée")
```

**Paramètres**
- **entity** : L'id de l'entité à tester.

**Retour**
- **static** : `true` si **entity** est statique, `false` sinon.

LeekScript : `isStatic()` — 15 opérations · https://leekwars.com/help/documentation/isStatic

### `Entity.birthTurn: int`

Renvoie le tour du combat où est apparue l'entité **entity**. Renvoie 1 s'il s'agit d'un poireau par exemple, et 5 s'il d'agit d'une invocation invoquée au tour 5.

**Paramètres**
- **entity** : L'id de l'entité dont le tour d'apparition sera renvoyé.

**Retour**
- **turn** : Le tour de combat où **entity** est apparue.

LeekScript : `getBirthTurn()` — 15 opérations · https://leekwars.com/help/documentation/getBirthTurn

### `Entity.turnOrder: int`

Retourne une valeur entre 1 et n (nombre d'entités actuellement en jeu) indiquant la position de l'entité **entity** dans l'ordre de jeu.

**Paramètres**
- **entity** : L'id de l'entité dont l'ordre de jeu sera renvoyé

**Retour**
- **turnOrder** : Place dans l'ordre de jeu de l'entité **entity**

LeekScript : `getEntityTurnOrder()` — 30 opérations · https://leekwars.com/help/documentation/getEntityTurnOrder

### `Entity.awakeningZone: int`

Renvoie le rayon de la zone d'Éveil de l'entité **entity**, en cases.

Une plante à zone ne joue pas de tour : elle se réveille quand une entité entre dans sa zone, et c'est à ce moment-là que son IA joue. La fonction renvoie `0` pour toute entité qui joue son tour normalement, y compris une plante enracinée sans zone d'Éveil.

Ni `getType` ni `getEntityTurnOrder` ne répondent à cette question : le type `ENTITY_PLANT` ne dit pas si la plante a une zone, et une plante à zone garde sa place dans l'ordre de jeu, seule son IA n'y est jamais lancée. La zone est un cercle mesuré en nombre de cases, comme `getCellDistance`, et toute case foulée compte : traverser la zone la réveille, même sans s'y arrêter.

Exemple :
```python
plant = Fight.getNearestEnemy()
if plant.awakeningZone > 0 and me.cell.distance(plant) <= plant.awakeningZone:
	Debug.log("Je suis dans la zone d'une plante !")
```

**Paramètres**
- **entity** *(optionnel)* : Identifiant de l'entité à interroger. Par défaut, l'entité courante.

**Retour**
- **zone** : Le rayon de la zone d'Éveil en cases, `0` si l'entité n'en a pas, ou `null` si l'entité n'existe pas.

LeekScript : `getAwakeningZone()` — 15 opérations · https://leekwars.com/help/documentation/getAwakeningZone

### `Entity.side: int`

Renvoie le coté de l'entité dans le combat en cours.

**Paramètres**
- **entity** : L'entité dont on cherche à connaitre le coté.

**Retour**
- **side** : Un nombre entre 0 et n, avec n le nombre d'équipes différentes dans le combat - 1.

A ne pas confondre avec `getTeamID`.

LeekScript : `getSide()` — 5 opérations · https://leekwars.com/help/documentation/getSide

### `Entity.leekID: int`

Renvoie l'id réel du poireau d'id **leek**.

**Paramètres**
- **entity** : L'id du poireau dont l'id réel sera retourné.

**Retour**
- **realID** : L'id réel du poireau **entity**.

LeekScript : `getLeekID()` — 15 opérations · https://leekwars.com/help/documentation/getLeekID

### `Entity.teamID: int`

Renvoie l'id de l'équipe de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont l'id d'équipe sera renvoyé.

**Retour**
- **id** : L'id de l'équipe de l'entité **entity**.

LeekScript : `getTeamID()` — 15 opérations · https://leekwars.com/help/documentation/getTeamID

### `Entity.teamName: str`

Renvoie le nom de l'équipe de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le nom d'équipe sera renvoyé.

**Retour**
- **name** : Le nom de l'équipe de l'entité **entity**.

LeekScript : `getTeamName()` — 15 opérations · https://leekwars.com/help/documentation/getTeamName

### `Entity.compositionName: str`

Renvoie le nom de la composition de l'entité **entity**, dans le contexte d'un combat d'équipe. Renvoie `null` si l'entité n'appartient pas à une composition.

**Paramètres**
- **entity** : L'id de l'entité dont le nom de composition sera renvoyé.

**Retour**
- **name** : Le nom de la composition de l'entité **entity**.

LeekScript : `getCompositionName()` — 15 opérations · https://leekwars.com/help/documentation/getCompositionName

### `Entity.farmerID: int`

Renvoie l'id de l'éleveur de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont l'id d'éleveur sera renvoyé.

**Retour**
- **id** : L'id de l'éleveur de l'entité **entity**.

LeekScript : `getFarmerID()` — 15 opérations · https://leekwars.com/help/documentation/getFarmerID

### `Entity.farmerName: str`

Renvoie le nom de l'éleveur de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le nom d'éleveur sera renvoyé.

**Retour**
- **name** : Le nom de de l'éleveur de l'entité **entity**.

LeekScript : `getFarmerName()` — 15 opérations · https://leekwars.com/help/documentation/getFarmerName

### `Entity.farmerCountry: str`

Renvoie le pays de l'éleveur de l'entité **entity**.

**Paramètres**
- **entity** : L'id de l'entité dont le pays de d'éleveur sera renvoyé.

**Retour**
- **country** : Le pays de l'éleveur de l'entité **entity**, ou "?" si non indiqué.

LeekScript : `getFarmerCountry()` — 15 opérations · https://leekwars.com/help/documentation/getFarmerCountry

### `Entity.aiID: int`

Renvoie l'id de l'IA de l'entité **entity**. Utilisez `getAIID` sans paramètre pour récupérer l'id de votre IA.

**Paramètres**
- **entity** : L'id de l'entité dont l'id d'IA sera renvoyé.

**Retour**
- **id** : L'id de l'IA de l'entité **entity**.

LeekScript : `getAIID()` — 15 opérations · https://leekwars.com/help/documentation/getAIID

### `Entity.aiName: str`

Renvoie le nom de l'IA de l'entité **entity**. Utilisez `getAIName()` sans paramètre pour récupérer le nom de votre IA.

**Paramètres**
- **entity** : L'id de l'entité dont le nom d'IA sera renvoyé.

**Retour**
- **name** : Le nom de l'IA de l'entité **entity**.

LeekScript : `getAIName()` — 15 opérations · https://leekwars.com/help/documentation/getAIName

### `Entity.isAlly() -> bool`

Détermine si l'entité **entity** est votre allié.

**Paramètres**
- **entity** : L'id de l'entité à tester.

**Retour**
- **isAlly** : `true` si l'entité **entity** est votre allié ou bien vous-même, `false` s'il s'agit d'un ennemi.

LeekScript : `isAlly()` — 15 opérations · https://leekwars.com/help/documentation/isAlly

### `Entity.isEnemy() -> bool`

Détermine si l'entité **entity** est votre ennemi.

**Paramètres**
- **entity** : L'id de l'entité à tester.

**Retour**
- **isEnemy** : `true` si l'entité **entity** est un ennemi, `false` s'il s'agit d'un allié ou bien vous-même.

LeekScript : `isEnemy()` — 15 opérations · https://leekwars.com/help/documentation/isEnemy

### `Entity.stat(stat: int) -> int`

Renvoie la valeur de la statistique **stat** de l'entité **entity**. Utilisez les constantes STAT_* pour spécifier la statistique (ex : STAT_STRENGTH, STAT_LIFE, etc.).

**Paramètres**
- **entity** : L'id de l'entité dont la statistique sera retournée.
- **stat** : La statistique à retourner (constante STAT_*).

**Retour**
- **value** : La valeur de la statistique **stat** de l'entité **entity**.

LeekScript : `getStat()` — 15 opérations · https://leekwars.com/help/documentation/getStat

### `Entity.get(id: int) -> Entity`

Entité d'id `id` (typée : Leek, Bulb, Mob...), ou None s'il est invalide.

### `Entity.distance(target: CellLike) -> int`

Retourne la distance entre deux cellules **cell1** et **cell2**.

La distance retournée est exprimée en nombre de cellules, et ne tient pas compte des divers obstacles entre les deux cellules.

Pour obtenir la distance à vol d'oiseau, voir `getDistance` et pour obtenir la distance du chemin entre les deux cellules en évitant les obstacles, voir `getPathLength`.

**Paramètres**
- **cell1** : L'id de la cellule de départ.
- **cell2** : L'id de la cellule d'arrivée.

**Retour**
- **distance**
	- Si les deux cellules sont valides : La distance entre les deux cellules cell1 et cell2.
	- Si une cellule est invalide, `-1`.

LeekScript : `getCellDistance()` — 15 opérations · https://leekwars.com/help/documentation/getCellDistance

## Bulb

### `Bulb.type: int`

Renvoie le type du bulbe **entity**, sous la forme de l'une des constantes `BULB_*` (par exemple `BULB_PUNY`, `BULB_FIRE`, `BULB_HEALER`...).

Si **entity** n'est pas précisée, c'est le type de l'entité courante qui est renvoyé. La fonction renvoie `-1` si l'entité existe mais n'est pas un bulbe, et `null` si aucune entité ne porte cet identifiant.

Exemple :
```python
enemy = Fight.getNearestEnemy()
# `type` n'existe que sur un Bulb : on vérifie le genre d'entité d'abord.
if enemy.entityType == Entity.Type.BULB and enemy.type == Bulb.Type.FIRE:
	Debug.log("Un bulbe de feu !")
```

**Paramètres**
- **entity** *(optionnel)* : Identifiant de l'entité à interroger. Par défaut, l'entité courante.

**Retour**
- **type** : Le type du bulbe (constante `BULB_*`), `-1` si l'entité n'est pas un bulbe, ou `null` si l'entité n'existe pas.

LeekScript : `getBulbType()` — 15 opérations · https://leekwars.com/help/documentation/getBulbType

## Chest

### `Chest.type: int`

Renvoie le type du coffre **entity**, sous la forme de l'une des constantes `CHEST_WOOD` (1), `CHEST_IRON` (2) ou `CHEST_DIAMOND` (3).

Si **entity** n'est pas précisée, c'est le type de l'entité courante qui est renvoyé. La fonction renvoie `-1` si l'entité existe mais n'est pas un coffre, et `null` si aucune entité ne porte cet identifiant.

Exemple :
```python
enemy = Fight.getNearestEnemy()
# `type` n'existe que sur un Chest : on vérifie le genre d'entité d'abord.
if enemy.entityType == Entity.Type.CHEST and enemy.type == Chest.Type.DIAMOND:
	Debug.log("Un coffre en diamant !")
```

**Paramètres**
- **entity** *(optionnel)* : Identifiant de l'entité à interroger. Par défaut, l'entité courante.

**Retour**
- **type** : Le type du coffre (`CHEST_WOOD`, `CHEST_IRON` ou `CHEST_DIAMOND`), `-1` si l'entité n'est pas un coffre, ou `null` si l'entité n'existe pas.

LeekScript : `getChestType()` — 15 opérations · https://leekwars.com/help/documentation/getChestType

## Mob

### `Mob.type: int`

Renvoie le type du mob **entity**, sous la forme de l'une des constantes `MOB_*` (par exemple `MOB_FENNEL_KING`, `MOB_EVIL_PUMPKIN`, `MOB_GRAAL`...).

Si **entity** n'est pas précisée, c'est le type de l'entité courante qui est renvoyé. La fonction renvoie `-1` si l'entité existe mais n'est pas un mob, et `null` si aucune entité ne porte cet identifiant.

Exemple :
```python
enemy = Fight.getNearestEnemy()
# `type` n'existe que sur un Mob : on vérifie le genre d'entité d'abord.
if enemy.entityType == Entity.Type.MOB and enemy.type == Mob.Type.FENNEL_KING:
	Debug.log("C'est le Roi Fenouil !")
```

**Paramètres**
- **entity** *(optionnel)* : Identifiant de l'entité à interroger. Par défaut, l'entité courante.

**Retour**
- **type** : Le type du mob (constante `MOB_*`), `-1` si l'entité n'est pas un mob, ou `null` si l'entité n'existe pas.

LeekScript : `getMobType()` — 15 opérations · https://leekwars.com/help/documentation/getMobType

## Plant

### `Plant.type: int`

Renvoie le type de plante de l'entité **entity**. Retourne -1 si l'entité n'est pas une plante. Utilisez les constantes PLANT_* pour comparer le résultat.

**Paramètres**
- **entity** : L'id de l'entité dont le type de plante sera renvoyé.

**Retour**
- **type** : Le type de plante de l'entité **entity**, ou -1 si ce n'est pas une plante.

LeekScript : `getPlantType()` — 15 opérations · https://leekwars.com/help/documentation/getPlantType

## Cell

### `Cell.id: int`

### `Cell.x: int`

Détermine la position en X de la cellule **cell**.

**Paramètres**
- **cell** : La cellule dont la position en X sera déterminée.

**Retour**
- **x** : La position en X de la cellule.

LeekScript : `getCellX()` — 5 opérations · https://leekwars.com/help/documentation/getCellX

### `Cell.y: int`

Détermine la position en Y de la cellule **cell**.

**Paramètres**
- **cell** : La cellule dont la position en Y sera déterminée.

**Retour**
- **y** : La position en Y de la cellule.

LeekScript : `getCellY()` — 5 opérations · https://leekwars.com/help/documentation/getCellY

### `Cell.empty: bool`

Détermine si une cellule est vide.

**Paramètres**
- **cell** : La cellule à tester.

**Retour**
- **empty** : `true` si la cellule est vide, `false` sinon.

LeekScript : `isEmptyCell()` — 10 opérations · https://leekwars.com/help/documentation/isEmptyCell

### `Cell.obstacle: bool`

Détermine si le contenu de la cellule **cell** est un obstacle.

**Paramètres**
- **cell** : La cellule à tester.

**Retour**
- **isObstacle** : `true` si la cellule contient un obstacle, `false` sinon.

LeekScript : `isObstacle()` — 10 opérations · https://leekwars.com/help/documentation/isObstacle

### `Cell.entity: Entity`

Renvoie l'entité qui se trouve sur la cellule **cell**.

**Paramètres**
- **cell** : La cellule dont on veut récupérer l'entité.

**Retour**
- **entity** : L'entité se trouvant sur la cellule.
	- `-1` si la cellule ne comporte pas d'entité.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getEntityOnCell()` — 15 opérations · https://leekwars.com/help/documentation/getEntityOnCell

### `Cell.hasEntity: bool`

Une entité (poireau, bulbe, tourelle...) occupe-t-elle la case.

Détermine si le contenu de la cellule **cell** est une entité.

*Exemple* :
```python
if cellule.hasEntity:
	# cette cellule contient une entité
```

**Paramètres**
- **cell** : La cellule à tester.

**Retour**
- **isEntity** : `true` si la cellule contient une entité, `false` sinon.

LeekScript : `isEntity()` — 10 opérations · https://leekwars.com/help/documentation/isEntity

### `Cell.content: int`

Retourne le contenu d'une cellule d'id **cell**.

**Paramètres**
- **cell** : L'id de la cellule dont le contenu sera retourné.

**Retour**
- **content** : Le contenu de la cellule **cell** : `CELL_EMPTY` pour une cellule vide, `CELL_ENTITY` pour une entité, `CELL_OBSTACLE` pour un obstacle.

LeekScript : `getCellContent()` — 6 opérations · https://leekwars.com/help/documentation/getCellContent

### `Cell.distance(target: CellLike) -> int`

Retourne la distance entre deux cellules **cell1** et **cell2**.

La distance retournée est exprimée en nombre de cellules, et ne tient pas compte des divers obstacles entre les deux cellules.

Pour obtenir la distance à vol d'oiseau, voir `getDistance` et pour obtenir la distance du chemin entre les deux cellules en évitant les obstacles, voir `getPathLength`.

**Paramètres**
- **cell1** : L'id de la cellule de départ.
- **cell2** : L'id de la cellule d'arrivée.

**Retour**
- **distance**
	- Si les deux cellules sont valides : La distance entre les deux cellules cell1 et cell2.
	- Si une cellule est invalide, `-1`.

LeekScript : `getCellDistance()` — 15 opérations · https://leekwars.com/help/documentation/getCellDistance

### `Cell.pathLength(target: CellLike, ignoredCells: list = ...) -> int`

Renvoie la longueur du chemin le plus court entre deux cellules **cell1** et **cell2**, en esquivant les obstacles, en ignorant les cellules contenues dans le tableau **ignoredCells**. Cette fonction équivaut à `count(getPath(cell1, cell2, ignoredCells))`.
Si un joueur se situe sur une cellule ignorée, le chemin peut passer sur lui.

La cellule de départ **cell1** n'est jamais comptée dans le résultat. La cellule **cell2** est comptée dans le résultat si et seulement si elle est vide ou ignorée par **ignoredCells**.

Si aucun chemin n'existe entre les deux cellules, **getPathLength** renvoie `null`.

**Paramètres**
- **cell1** : La cellule de départ.
- **cell2** : La cellule d'arrivée.
- **ignoredCells** : Le tableau des cellules à ignorer. Par défaut une liste vide.

**Retour**
- **length**
	- Si un chemin existe : la longueur du chemin entre **cell1** et **cell2**.
	- Si le chemin n'a pas été trouvé : `null`.

LeekScript : `getPathLength()` — -1 opérations · https://leekwars.com/help/documentation/getPathLength

### `Cell.lineOfSight(target: CellLike, ignoredEntities: Any = ...) -> bool`

Vérifie la ligne de vue entre la cellule **start** et la cellule **end**, en ignorant les entitées dans le tableau **entityToIgnore**.

*Exemple* : `if (lineOfSight(getCell(), getCell(enemy))`

L'algorithme se décrit comme suit :
- Tracer un segment entre les centres des deux cellules testées.
- Faire la liste des cellules traversées par ce segment. Une cellule n'est pas considérée comme traversée si le segment frôle son bord, ou bien si elle est ignorée.
- Si une seule de ces cellules traversée est un obstacle ou contient une entité, la ligne de vue est bloquée, sinon elle est dégagée.

**Paramètres**
- **start** : Cellule de départ.
- **end** : Cellule cible.
- **entityToIgnore** (optionnel) : Entité à ignorer ou tableau d'entitées à ignorer, par défaut, votre entité est ignorée.

**Retour**
- **los** : (booléen)
	- `null` si **start** ou **end** n'est pas une cellule de la carte ;
	- `true` si la ligne de vue est dégagée ;
	- `false` sinon.

**Démonstration**
Cliquez sur une cellule pour afficher toutes les cellules qui sont en ligne de vue avec.

{{ line-of-sight }}

**Implémentation mathématique**
Le lineOfSight utilise un algorithme inspiré de l'algorithme de tracé de ligne de bresenham ([wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_trac%C3%A9_de_segment_de_Bresenham))

LeekScript : `lineOfSight()` — 31 opérations · https://leekwars.com/help/documentation/lineOfSight

### `Cell.path(target: CellLike, ignoredCells: list = ...) -> list[Cell]`

Renvoie le plus court chemin en évitant les obstacles entre deux cellules **cell1** et **cell2**, si celui-ci existe, en ignorant les cellules contenues dans le tableau **ignoredCells**.

La cellule de départ **cell1** ne fait jamais partie du chemin résultant. La cellule **cell2** fait partie du chemin résultant si et seulement si elle est vide.

Si aucun chemin n'existe entre les deux cellules, **getPath** renvoie `null`.

Attention, il est possible que `getPath(cell1, cell2) != getPath(cell2, cell1)`.

**Paramètres**
- **start** : La cellule de départ.
- **end** : La cellule d'arrivée.
- **ignoredCells** : Le tableau des cellules à ignorer. Par défaut une liste vide.

**Retour**
- **path**
	- Si un chemin existe : un tableau contenant les cellules constituant le chemin entre les deux cellules
	- Si le chemin n'a pas été trouvé : `null`.

**Exemples**
```python
path = Field.path(Fight.me.cell, enemy.cell)
Debug.mark(path, Color.RED)  # Affiche le chemin entre moi et l'ennemi
```

LeekScript : `getPath()` — -1 opérations · https://leekwars.com/help/documentation/getPath

### `Cell.onSameLine(target: CellLike) -> bool`

Détermine si deux cellules **cell1** et **cell2** sont sur la même ligne.

**Paramètres**
- **cell1** : La première cellule.
- **cell2** : La deuxième cellule.

**Retour**
- **sameLine** : `true` si les deux cellules sont sur la même ligne, `false` sinon.

LeekScript : `isOnSameLine()` — 15 opérations · https://leekwars.com/help/documentation/isOnSameLine

### `Cell.get(id: int) -> Cell`

Cellule d'id `id`, ou None s'il est invalide (chemin inverse : relire un id rangé dans un registre).

## Field

### `Field.type: int`

Renvoie le type de terrain sur lequel se déroule le combat (usine, désert, forêt etc.), parmi les constantes `MAP_NEXUS`, `MAP_FACTORY`, `MAP_DESERT`, `MAP_FOREST`, `MAP_GLACIER` et `MAP_BEACH`.

**Retour**
- **mapType** : Le type de terrain.

LeekScript : `getMapType()` — 5 opérations · https://leekwars.com/help/documentation/getMapType

### `Field.cellFromXY(x: int, y: int) -> Cell`

Retourne la cellule se trouvant à la position (**x**, **y**).

**Paramètres**
- **x** : La position en x de la cellule.
- **y** : La position en y de la cellule.

**Retour**
- **cell** : La cellule à la position (**x**, **y**), **null** si la cellule n'existe pas.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

LeekScript : `getCellFromXY()` — 5 opérations · https://leekwars.com/help/documentation/getCellFromXY

### `Field.getObstacles() -> list[Cell]`

Renvoie la liste des cases obstacles du terrain.

**Retour**
- **obstacles** : Le tableau contenant les cellules obstacles.

LeekScript : `getObstacles()` — 85 opérations · https://leekwars.com/help/documentation/getObstacles

### `Field.distance(a: CellLike, b: CellLike) -> int`

Retourne la distance entre deux cellules **cell1** et **cell2**.

La distance retournée est exprimée en nombre de cellules, et ne tient pas compte des divers obstacles entre les deux cellules.

Pour obtenir la distance à vol d'oiseau, voir `getDistance` et pour obtenir la distance du chemin entre les deux cellules en évitant les obstacles, voir `getPathLength`.

**Paramètres**
- **cell1** : L'id de la cellule de départ.
- **cell2** : L'id de la cellule d'arrivée.

**Retour**
- **distance**
	- Si les deux cellules sont valides : La distance entre les deux cellules cell1 et cell2.
	- Si une cellule est invalide, `-1`.

LeekScript : `getCellDistance()` — 15 opérations · https://leekwars.com/help/documentation/getCellDistance

### `Field.cellDistance(a: CellLike, b: CellLike) -> int`

Retourne la distance entre deux cellules **cell1** et **cell2**.

La distance retournée est exprimée en nombre de cellules, et ne tient pas compte des divers obstacles entre les deux cellules.

Pour obtenir la distance à vol d'oiseau, voir `getDistance` et pour obtenir la distance du chemin entre les deux cellules en évitant les obstacles, voir `getPathLength`.

**Paramètres**
- **cell1** : L'id de la cellule de départ.
- **cell2** : L'id de la cellule d'arrivée.

**Retour**
- **distance**
	- Si les deux cellules sont valides : La distance entre les deux cellules cell1 et cell2.
	- Si une cellule est invalide, `-1`.

LeekScript : `getCellDistance()` — 15 opérations · https://leekwars.com/help/documentation/getCellDistance

### `Field.euclideanDistance(a: CellLike, b: CellLike) -> float`

Calcule la distance à vol d'oiseau entre deux cellules **cell1** et **cell2**.

Pour obtenir la distance en nombre de cellules, voir `getCellDistance`, et pour obtenir la longueur du chemin entre les deux cellules en esquivant les divers obstacles, voir `getPathLength`.

**Paramètres**
- **cell1** : La cellule de départ.
- **cell2** : La cellule d'arrivée.

**Retour**
- **distance** : La distance à vol d'oiseau entre les deux cellules.

LeekScript : `getDistance()` — 15 opérations · https://leekwars.com/help/documentation/getDistance

### `Field.pathLength(a: CellLike, b: CellLike, ignoredCells: list = ...) -> int`

Renvoie la longueur du chemin le plus court entre deux cellules **cell1** et **cell2**, en esquivant les obstacles, en ignorant les cellules contenues dans le tableau **ignoredCells**. Cette fonction équivaut à `count(getPath(cell1, cell2, ignoredCells))`.
Si un joueur se situe sur une cellule ignorée, le chemin peut passer sur lui.

La cellule de départ **cell1** n'est jamais comptée dans le résultat. La cellule **cell2** est comptée dans le résultat si et seulement si elle est vide ou ignorée par **ignoredCells**.

Si aucun chemin n'existe entre les deux cellules, **getPathLength** renvoie `null`.

**Paramètres**
- **cell1** : La cellule de départ.
- **cell2** : La cellule d'arrivée.
- **ignoredCells** : Le tableau des cellules à ignorer. Par défaut une liste vide.

**Retour**
- **length**
	- Si un chemin existe : la longueur du chemin entre **cell1** et **cell2**.
	- Si le chemin n'a pas été trouvé : `null`.

LeekScript : `getPathLength()` — -1 opérations · https://leekwars.com/help/documentation/getPathLength

### `Field.lineOfSight(a: CellLike, b: CellLike, ignoredEntities: Any = ...) -> bool`

Vérifie la ligne de vue entre la cellule **start** et la cellule **end**, en ignorant les entitées dans le tableau **entityToIgnore**.

*Exemple* : `if (lineOfSight(getCell(), getCell(enemy))`

L'algorithme se décrit comme suit :
- Tracer un segment entre les centres des deux cellules testées.
- Faire la liste des cellules traversées par ce segment. Une cellule n'est pas considérée comme traversée si le segment frôle son bord, ou bien si elle est ignorée.
- Si une seule de ces cellules traversée est un obstacle ou contient une entité, la ligne de vue est bloquée, sinon elle est dégagée.

**Paramètres**
- **start** : Cellule de départ.
- **end** : Cellule cible.
- **entityToIgnore** (optionnel) : Entité à ignorer ou tableau d'entitées à ignorer, par défaut, votre entité est ignorée.

**Retour**
- **los** : (booléen)
	- `null` si **start** ou **end** n'est pas une cellule de la carte ;
	- `true` si la ligne de vue est dégagée ;
	- `false` sinon.

**Démonstration**
Cliquez sur une cellule pour afficher toutes les cellules qui sont en ligne de vue avec.

{{ line-of-sight }}

**Implémentation mathématique**
Le lineOfSight utilise un algorithme inspiré de l'algorithme de tracé de ligne de bresenham ([wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_trac%C3%A9_de_segment_de_Bresenham))

LeekScript : `lineOfSight()` — 31 opérations · https://leekwars.com/help/documentation/lineOfSight

### `Field.onSameLine(a: CellLike, b: CellLike) -> bool`

Détermine si deux cellules **cell1** et **cell2** sont sur la même ligne.

**Paramètres**
- **cell1** : La première cellule.
- **cell2** : La deuxième cellule.

**Retour**
- **sameLine** : `true` si les deux cellules sont sur la même ligne, `false` sinon.

LeekScript : `isOnSameLine()` — 15 opérations · https://leekwars.com/help/documentation/isOnSameLine

### `Field.path(a: CellLike, b: CellLike, ignoredCells: list = ...) -> list[Cell]`

Renvoie le plus court chemin en évitant les obstacles entre deux cellules **cell1** et **cell2**, si celui-ci existe, en ignorant les cellules contenues dans le tableau **ignoredCells**.

La cellule de départ **cell1** ne fait jamais partie du chemin résultant. La cellule **cell2** fait partie du chemin résultant si et seulement si elle est vide.

Si aucun chemin n'existe entre les deux cellules, **getPath** renvoie `null`.

Attention, il est possible que `getPath(cell1, cell2) != getPath(cell2, cell1)`.

**Paramètres**
- **start** : La cellule de départ.
- **end** : La cellule d'arrivée.
- **ignoredCells** : Le tableau des cellules à ignorer. Par défaut une liste vide.

**Retour**
- **path**
	- Si un chemin existe : un tableau contenant les cellules constituant le chemin entre les deux cellules
	- Si le chemin n'a pas été trouvé : `null`.

**Exemples**
```python
path = Field.path(Fight.me.cell, enemy.cell)
Debug.mark(path, Color.RED)  # Affiche le chemin entre moi et l'ennemi
```

LeekScript : `getPath()` — -1 opérations · https://leekwars.com/help/documentation/getPath

### `Field.NEXUS: int`

(= 1)

LeekScript : `MAP_NEXUS`

### `Field.FACTORY: int`

(= 2)

LeekScript : `MAP_FACTORY`

### `Field.DESERT: int`

(= 3)

LeekScript : `MAP_DESERT`

### `Field.FOREST: int`

(= 4)

LeekScript : `MAP_FOREST`

### `Field.GLACIER: int`

(= 5)

LeekScript : `MAP_GLACIER`

### `Field.BEACH: int`

(= 6)

LeekScript : `MAP_BEACH`

### `Field.TEMPLE: int`

(= 7)

LeekScript : `MAP_TEMPLE`

### `Field.CASTLE: int`

(= 9)

LeekScript : `MAP_CASTLE`

### `Field.CEMETERY: int`

(= 10)

LeekScript : `MAP_CEMETERY`

### `Field.TEIEN: int`

(= 8)

LeekScript : `MAP_TEIEN`

## Item

### `Item.id: int`

### `Item.cost: int`

Renvoie le coût en PT de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont le coût sera renvoyé.

**Retour**
- **cost** : Le coût en PT de l'arme **weapon**.

LeekScript : `getWeaponCost()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponCost

### `Item.minRange: int`

Renvoie la portée minimale de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont la portée minimale sera renvoyée.

**Retour**
- **minRange** : La portée minimale de l'arme **weapon**.

LeekScript : `getWeaponMinRange()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponMinRange

### `Item.maxRange: int`

Renvoie la portée maximale de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont la portée maximale sera renvoyée.

**Retour**
- **maxRange** : La portée maximale de l'arme **weapon**.

LeekScript : `getWeaponMaxRange()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponMaxRange

### `Item.name: str`

Nom de l'arme / de la puce.

Renvoie le nom de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont le nom sera renvoyé.

**Retour**
- **name** : Le nom de l'arme **weapon**.

LeekScript : `getWeaponName()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponName

### `Item.area: int`

Renvoie le type de zone d'effet de l'arme **weapon**.

**Paramètres**
- **weapon** : L'arme dont le type de zone sera renvoyé.

**Retour**
- **area** : Le type de zone de l'arme **weapon** parmi les constantes AREA_* :
  - `AREA_POINT` : zone d'une seule case
  - `AREA_LASER_LINE` : ligne d'un laser
  - `AREA_CIRCLE_1` : zone circulaire de 3 cases de diamètre
  - `AREA_CIRCLE_2` : zone circulaire de 5 cases de diamètre
  - `AREA_CIRCLE_3` : zone circulaire de 7 cases de diamètre
  - etc.

LeekScript : `getWeaponArea()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponArea

### `Item.launchType: int`

Renvoie le mode de lancé de l'arme **weapon**, parmi les constantes LAUNCH_TYPE_*.

**Paramètres**
- **weapon** : L'id de l'arme dont le mode de lancé sera renvoyé. Par défaut votre arme actuellement équipée.

**Retour**
- **launchType** : Le mode de lancé de l'arme **weapon**.

LeekScript : `getWeaponLaunchType()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponLaunchType

### `Item.maxUses: int`

Renvoie le nombre maximum d'utilisations possibles d'une arme sur un tour.

**Paramètres**
- **weapon** : L'arme à tester.

**Retour**
- **maxUses** : Le nombre d'utilisations possibles, -1 s'il n'y a pas de limite.

LeekScript : `getWeaponMaxUses()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponMaxUses

### `Item.inline: bool`

L'item se lance en ligne (tir en ligne).

Détermine si l'arme **weapon** peut être utilisée uniquement en ligne.

**Paramètres**
- **weapon** : L'id de l'arme à tester.

**Retour**
- **isInline** : `true` si l'arme est utilisable uniquement en ligne, `false` sinon.

LeekScript : `isInlineWeapon()` — 10 opérations · https://leekwars.com/help/documentation/isInlineWeapon

### `Item.needsLos: bool`

L'item exige une ligne de vue.

Renvoie si l'arme **weapon** a besoin d'une ligne de vue pour tirer.

**Paramètres**
- **weapon** : L'id de l'arme à tester.

**Retour**
- **needLos** : `true` si l'arme **weapon** a besoin d'une ligne de vue pour tirer, `false` sinon.

LeekScript : `weaponNeedLos()` — 10 opérations · https://leekwars.com/help/documentation/weaponNeedLos

### `Item.failure: int`

Renvoie le pourcentage de risque d'échec de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont le pourcentage d'échec sera renvoyé.

**Retour**
- **failure** : Pourcentage d'échec de l'arme **weapon**, un nombre entier entre **0** et **100**.

LeekScript : `getWeaponFailure()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponFailure

### `Item.features: list[Feature]`

Caractéristiques déclarées de l'item (list[Feature] : dégâts, poison, téléport...). Distinct de entity.effects (effets ACTIFS).

Renvoie les effets de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont les effets seront retournés.

**Retour**
- **effects** : Un tableau contenant les effets de l'arme **weapon**. Chaque effet est lui-même un tableau de la forme
[type, min, max, turns, targets, modifiers].
	- **type** est une constante parmis les constantes d'effet : EFFECT_DAMAGE, `EFFECT_HEAL`, `EFFECT_ABSOLUTE_SHIELD`, `EFFECT_RELATIVE_SHIELD`, `EFFECT_DEBUFF`, `EFFECT_BUFF_STRENGTH`, `EFFECT_BUFF_AGILITY`, `EFFECT_BUFF_MP`, `EFFECT_BUFF_TP` etc.
	- **min** et **max** sont la valeur minimum et maximum de l'effet (comme indiqué dans le marché).
	- **turns** est la durée de l'effet en nombre de tours.
	- **targets** représente les joueurs qui seront touchés par cet effet dans la zone. Il s'agit d'une combinaison binaire des constantes :
		- `EFFECT_TARGET_ALLIES` : Affecte les alliés
		- `EFFECT_TARGET_ENEMIES` : Affecte les ennemis
		- `EFFECT_TARGET_CASTER` : Affecte le lanceur
		- `EFFECT_TARGET_SUMMONS` : Affecte les invocations
		- `EFFECT_TARGET_NON_SUMMONS` : Affecte les entités non invoquées
	- **modifiers** représente les modificateurs de l'effet. Il s'agit d'une combinaison binaire des constantes :
		- `EFFECT_MODIFIER_STACKABLE` : L'effet est cumulable.
		- `EFFECT_MODIFIER_MULTIPLIED_BY_TARGETS` : L'effet est multiplié par le nombre de cibles touchées dans la zone.
		- `EFFECT_MODIFIER_ON_CASTER` : Affecte toujours le lanceur.

**Exemples**
Récupérer les dégâts moyens d'une arme :
```python
# `features` expose des objets nommés : minValue/maxValue plutôt que [1] et [2].
features = Weapon.pistol.features
dégâtsMoyens = (features[0].minValue + features[0].maxValue) / 2
```

Lire les cibles *targets* :
```python
if targets & Effect.Target.ALLIES: Debug.log('Affecte les alliés')
if targets & Effect.Target.ENEMIES: Debug.log('Affecte les ennemis')
if targets & Effect.Target.CASTER: Debug.log('Affecte le lanceur')
if targets & Effect.Target.SUMMONS: Debug.log('Affecte les invocations')
if targets & Effect.Target.NON_SUMMONS: Debug.log('Affecte les non-invocations (poireaux, mobs...)')
```

Lire les modificateurs :
On peut lire cette valeur de la manière suivante :
```python
if modifiers & Effect.Modifier.STACKABLE: Debug.log("L'effet est cumulable")
if modifiers & Effect.Modifier.MULTIPLIED_BY_TARGETS: Debug.log("L'effet est multiplié par le nombre de cibles")
if modifiers & Effect.Modifier.ON_CASTER: Debug.log("Affecte le lanceur")
```

LeekScript : `getWeaponEffects()` — 125 opérations · https://leekwars.com/help/documentation/getWeaponEffects

### `Item.effectiveArea(cell: CellLike, frm: CellLike = ...) -> list[Cell]`

Zone d'effet réelle de l'item sur `cell`, lancé depuis `frm` (défaut : position courante). list[Cell].

Renvoie la liste des cellules qui seront affectées si l'arme **weapon** est utilisée sur la cellule **cell** depuis la cellule **from**.
La fonction ne vérifie pas s'il est possible de tirer sur la cellule **cell** ou de se rendre sur la cellule **from**.

**Paramètres**
- **weapon** : L'arme à tester.
- **cell** : La cellule cible.
- **from** : La cellule depuis laquelle l'arme est utilisée.

**Retour**
- **cells** : Le tableau contenant toutes les cellules qui seront affectées.

LeekScript : `getWeaponEffectiveArea()` — 78 opérations · https://leekwars.com/help/documentation/getWeaponEffectiveArea

### `Item.get(id: int) -> Weapon | Chip`

L'item (arme OU puce) d'id `id`, ou None. Weapon.get / Chip.get restreignent à leur type.

## Weapon

### `Weapon.cost: int`

Renvoie le coût en PT de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont le coût sera renvoyé.

**Retour**
- **cost** : Le coût en PT de l'arme **weapon**.

LeekScript : `getWeaponCost()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponCost

### `Weapon.minRange: int`

Renvoie la portée minimale de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont la portée minimale sera renvoyée.

**Retour**
- **minRange** : La portée minimale de l'arme **weapon**.

LeekScript : `getWeaponMinRange()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponMinRange

### `Weapon.maxRange: int`

Renvoie la portée maximale de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont la portée maximale sera renvoyée.

**Retour**
- **maxRange** : La portée maximale de l'arme **weapon**.

LeekScript : `getWeaponMaxRange()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponMaxRange

### `Weapon.name: str`

Renvoie le nom de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont le nom sera renvoyé.

**Retour**
- **name** : Le nom de l'arme **weapon**.

LeekScript : `getWeaponName()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponName

### `Weapon.area: int`

Renvoie le type de zone d'effet de l'arme **weapon**.

**Paramètres**
- **weapon** : L'arme dont le type de zone sera renvoyé.

**Retour**
- **area** : Le type de zone de l'arme **weapon** parmi les constantes AREA_* :
  - `AREA_POINT` : zone d'une seule case
  - `AREA_LASER_LINE` : ligne d'un laser
  - `AREA_CIRCLE_1` : zone circulaire de 3 cases de diamètre
  - `AREA_CIRCLE_2` : zone circulaire de 5 cases de diamètre
  - `AREA_CIRCLE_3` : zone circulaire de 7 cases de diamètre
  - etc.

LeekScript : `getWeaponArea()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponArea

### `Weapon.launchType: int`

Renvoie le mode de lancé de l'arme **weapon**, parmi les constantes LAUNCH_TYPE_*.

**Paramètres**
- **weapon** : L'id de l'arme dont le mode de lancé sera renvoyé. Par défaut votre arme actuellement équipée.

**Retour**
- **launchType** : Le mode de lancé de l'arme **weapon**.

LeekScript : `getWeaponLaunchType()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponLaunchType

### `Weapon.maxUses: int`

Renvoie le nombre maximum d'utilisations possibles d'une arme sur un tour.

**Paramètres**
- **weapon** : L'arme à tester.

**Retour**
- **maxUses** : Le nombre d'utilisations possibles, -1 s'il n'y a pas de limite.

LeekScript : `getWeaponMaxUses()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponMaxUses

### `Weapon.inline: bool`

Détermine si l'arme **weapon** peut être utilisée uniquement en ligne.

**Paramètres**
- **weapon** : L'id de l'arme à tester.

**Retour**
- **isInline** : `true` si l'arme est utilisable uniquement en ligne, `false` sinon.

LeekScript : `isInlineWeapon()` — 10 opérations · https://leekwars.com/help/documentation/isInlineWeapon

### `Weapon.needsLos: bool`

Renvoie si l'arme **weapon** a besoin d'une ligne de vue pour tirer.

**Paramètres**
- **weapon** : L'id de l'arme à tester.

**Retour**
- **needLos** : `true` si l'arme **weapon** a besoin d'une ligne de vue pour tirer, `false` sinon.

LeekScript : `weaponNeedLos()` — 10 opérations · https://leekwars.com/help/documentation/weaponNeedLos

### `Weapon.failure: int`

Renvoie le pourcentage de risque d'échec de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont le pourcentage d'échec sera renvoyé.

**Retour**
- **failure** : Pourcentage d'échec de l'arme **weapon**, un nombre entier entre **0** et **100**.

LeekScript : `getWeaponFailure()` — 15 opérations · https://leekwars.com/help/documentation/getWeaponFailure

### `Weapon.features: list[Feature]`

Renvoie les effets de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont les effets seront retournés.

**Retour**
- **effects** : Un tableau contenant les effets de l'arme **weapon**. Chaque effet est lui-même un tableau de la forme
[type, min, max, turns, targets, modifiers].
	- **type** est une constante parmis les constantes d'effet : EFFECT_DAMAGE, `EFFECT_HEAL`, `EFFECT_ABSOLUTE_SHIELD`, `EFFECT_RELATIVE_SHIELD`, `EFFECT_DEBUFF`, `EFFECT_BUFF_STRENGTH`, `EFFECT_BUFF_AGILITY`, `EFFECT_BUFF_MP`, `EFFECT_BUFF_TP` etc.
	- **min** et **max** sont la valeur minimum et maximum de l'effet (comme indiqué dans le marché).
	- **turns** est la durée de l'effet en nombre de tours.
	- **targets** représente les joueurs qui seront touchés par cet effet dans la zone. Il s'agit d'une combinaison binaire des constantes :
		- `EFFECT_TARGET_ALLIES` : Affecte les alliés
		- `EFFECT_TARGET_ENEMIES` : Affecte les ennemis
		- `EFFECT_TARGET_CASTER` : Affecte le lanceur
		- `EFFECT_TARGET_SUMMONS` : Affecte les invocations
		- `EFFECT_TARGET_NON_SUMMONS` : Affecte les entités non invoquées
	- **modifiers** représente les modificateurs de l'effet. Il s'agit d'une combinaison binaire des constantes :
		- `EFFECT_MODIFIER_STACKABLE` : L'effet est cumulable.
		- `EFFECT_MODIFIER_MULTIPLIED_BY_TARGETS` : L'effet est multiplié par le nombre de cibles touchées dans la zone.
		- `EFFECT_MODIFIER_ON_CASTER` : Affecte toujours le lanceur.

**Exemples**
Récupérer les dégâts moyens d'une arme :
```python
# `features` expose des objets nommés : minValue/maxValue plutôt que [1] et [2].
features = Weapon.pistol.features
dégâtsMoyens = (features[0].minValue + features[0].maxValue) / 2
```

Lire les cibles *targets* :
```python
if targets & Effect.Target.ALLIES: Debug.log('Affecte les alliés')
if targets & Effect.Target.ENEMIES: Debug.log('Affecte les ennemis')
if targets & Effect.Target.CASTER: Debug.log('Affecte le lanceur')
if targets & Effect.Target.SUMMONS: Debug.log('Affecte les invocations')
if targets & Effect.Target.NON_SUMMONS: Debug.log('Affecte les non-invocations (poireaux, mobs...)')
```

Lire les modificateurs :
On peut lire cette valeur de la manière suivante :
```python
if modifiers & Effect.Modifier.STACKABLE: Debug.log("L'effet est cumulable")
if modifiers & Effect.Modifier.MULTIPLIED_BY_TARGETS: Debug.log("L'effet est multiplié par le nombre de cibles")
if modifiers & Effect.Modifier.ON_CASTER: Debug.log("Affecte le lanceur")
```

LeekScript : `getWeaponEffects()` — 125 opérations · https://leekwars.com/help/documentation/getWeaponEffects

### `Weapon.passiveFeatures: list[Feature]`

Renvoie les effets passifs de l'arme **weapon**.

**Paramètres**
- **weapon** : L'id de l'arme dont les effets passifs seront retournés.

**Retour**
- **passiveEffects** : Un tableau contenant les effets de l'arme **weapon**. Chaque effet est lui-même un tableau de la forme
`[type, min, max, turns, targets, modifiers]`. Ces effets sont les mêmes que ceux renvoyés par `getWeaponEffects`.
Si il n'y a pas d'effets passifs, une liste vide est renvoyée.

LeekScript : `getWeaponPassiveEffects()` — 125 opérations · https://leekwars.com/help/documentation/getWeaponPassiveEffects

### `Weapon.effectiveArea(cell: CellLike, frm: CellLike = ...) -> list[Cell]`

Renvoie la liste des cellules qui seront affectées si l'arme **weapon** est utilisée sur la cellule **cell** depuis la cellule **from**.
La fonction ne vérifie pas s'il est possible de tirer sur la cellule **cell** ou de se rendre sur la cellule **from**.

**Paramètres**
- **weapon** : L'arme à tester.
- **cell** : La cellule cible.
- **from** : La cellule depuis laquelle l'arme est utilisée.

**Retour**
- **cells** : Le tableau contenant toutes les cellules qui seront affectées.

LeekScript : `getWeaponEffectiveArea()` — 78 opérations · https://leekwars.com/help/documentation/getWeaponEffectiveArea

### `Weapon.get(id: int) -> Weapon`

L'arme d'id `id`, ou None si l'id n'est pas celui d'une arme.

### `Weapon.getAll() -> list[Weapon]`

Retourne la liste de toutes les armes du jeu.

**Retour**
- **weapons** : La liste de toutes les armes du jeu.

LeekScript : `getAllWeapons()` — 200 opérations · https://leekwars.com/help/documentation/getAllWeapons

### `Weapon.isWeapon(value: Any) -> bool`

Détermine si une valeur est une constante représentant une arme.
```python
Weapon.isWeapon(Weapon.laser)   # True
Weapon.isWeapon(Chip.teleportation) # False
```

**Paramètres**
- **value** : Le nombre à déterminer.

**Retour**
- **weapon** : `true` si la valeur est une constante d'arme.

LeekScript : `isWeapon()` — 15 opérations · https://leekwars.com/help/documentation/isWeapon

## Chip

### `Chip.cost: int`

Renvoie le coût en PT de la puce **chip**.

**Paramètres**
- **chip** : La puce dont le coût sera renvoyé.

**Retour**
- **cost** : Le coût de la puce **chip**.

LeekScript : `getChipCost()` — 15 opérations · https://leekwars.com/help/documentation/getChipCost

### `Chip.cooldown: int`

Renvoie le temps de récupération de la puce **chip**, issu du marché.

**Paramètres**
- **chip** : La puce dont le cooldown sera renvoyé.

**Retour**
- **cooldown** : Le cooldown de la puce **chip**. Pour les puces à cooldown infini comme Régénération, renvoie `-1`.

LeekScript : `getChipCooldown()` — 15 opérations · https://leekwars.com/help/documentation/getChipCooldown

### `Chip.currentCooldown: int`

Renvoie le cooldown actuel de la puce **chip** de l'entité **entity**.

Il s'agit du nombre de tours avant lesquels la puce deviendra utilisable, `0` si elle est actuellement utilisable. Pour les puces à cooldown infini comme `Régénération`, renvoie un nombre supérieur à `MAX_TURNS` après utilisation.

**Paramètres**
- **chip** : La puce dont le cooldown actuel sera renvoyé.
- **entity** : L'entité dont le cooldown sera renvoyé.

**Retour**
- **cooldown** : Le cooldown actuel de la puce **chip**.

LeekScript : `getCooldown()` — 30 opérations · https://leekwars.com/help/documentation/getCooldown

### `Chip.minRange: int`

Renvoie la portée minimale de la puce **chip**.

**Paramètres**
- **chip** : La puce dont la portée minimale sera renvoyée.

**Retour**
- **minRange** : La portée minimale de la puce **chip**.

LeekScript : `getChipMinRange()` — 15 opérations · https://leekwars.com/help/documentation/getChipMinRange

### `Chip.maxRange: int`

Renvoie la portée maximale de la puce **chip**.

**Paramètres**
- **chip** : La puce dont la portée maximale sera renvoyée.

**Retour**
- **maxRange** : La portée maximale de la puce **chip**.

LeekScript : `getChipMaxRange()` — 15 opérations · https://leekwars.com/help/documentation/getChipMaxRange

### `Chip.minScope: int`

Renvoie la portée minimale de la puce **chip**.

**Paramètres**
- **chip** : La puce dont la portée minimale sera renvoyée.

**Retour**
- **minScope** : La portée minimale de la puce **chip**.

LeekScript : `getChipMinScope()` — 15 opérations · https://leekwars.com/help/documentation/getChipMinScope

### `Chip.maxScope: int`

Renvoie la portée maximale de la puce **chip**.

**Paramètres**
- **chip** : La puce dont la portée maximale sera renvoyée.

**Retour**
- **maxScope** : La portée maximale de la puce **chip**.

LeekScript : `getChipMaxScope()` — 15 opérations · https://leekwars.com/help/documentation/getChipMaxScope

### `Chip.name: str`

Renvoie le nom de la puce **chip**.

**Paramètres**
- **chip** : La puce dont le nom sera renvoyé.

**Retour**
- **name** : Le nom de la puce **chip**.

LeekScript : `getChipName()` — 15 opérations · https://leekwars.com/help/documentation/getChipName

### `Chip.area: int`

Renvoie le type de zone d'effet de de la puce **chip**.

**Paramètres**
- **chip** : La puce dont le type de zone sera renvoyé.

**Retour**
- **area** : Le type de zone de la puce **chip** parmi les constantes AREA_* :
  - `AREA_POINT` : zone d'une seule case
  - `AREA_LASER_LINE` : ligne d'un laser
  - `AREA_CIRCLE_1` : zone circulaire de 3 cases de diamètre
  - `AREA_CIRCLE_2` : zone circulaire de 5 cases de diamètre
  - `AREA_CIRCLE_3` : zone circulaire de 7 cases de diamètre
  - etc.

LeekScript : `getChipArea()` — 15 opérations · https://leekwars.com/help/documentation/getChipArea

### `Chip.launchType: int`

Renvoie le mode de lancé de la puce **chip**, parmi les constantes LAUNCH_TYPE_*.

**Paramètres**
- **chip** : L'id de la puce dont le mode de lancé sera renvoyé.

**Retour**
- **launchType** : Le mode de lancé de la puce **chip**.

LeekScript : `getChipLaunchType()` — 15 opérations · https://leekwars.com/help/documentation/getChipLaunchType

### `Chip.maxUses: int`

Renvoie le nombre maximum d'utilisations possibles d'une puce sur un tour. Attention, la puce peut aussi être limitée par son délai de récupération.

**Paramètres**
- **chip** : La puce à tester.

**Retour**
- **maxUses** : Le nombre d'utilisations possibles, -1 s'il n'y a pas de limite.
Attention, s'il y a un temps de récupération (cooldown), cette fonction renverra -1 malgré qu'il ne soit possible de lancer la puce qu'une fois dans le tour (à cause de ce temps de récupération).

LeekScript : `getChipMaxUses()` — 15 opérations · https://leekwars.com/help/documentation/getChipMaxUses

### `Chip.inline: bool`

Détermine si la puce **chip** peut être utlisée uniquement en ligne.

**Paramètres**
- **chip** : L'id de la puce à tester.

**Retour**
- **isInline** : `true` si la puce est utilisable uniquement en ligne, `false` sinon.

LeekScript : `isInlineChip()` — 10 opérations · https://leekwars.com/help/documentation/isInlineChip

### `Chip.needsLos: bool`

Renvoie si la puce **chip** a besoin d'une ligne de vue pour être utilisée.

**Paramètres**
- **chip** : L'id de la puce à tester.

**Retour**
- **needLos** : `true` si la puce **chip** a besoin d'une ligne de vue pour être utilisée, `false` sinon.

LeekScript : `chipNeedLos()` — 10 opérations · https://leekwars.com/help/documentation/chipNeedLos

### `Chip.failure: int`

Renvoie le pourcentage de risque d'échec de la puce **chip**.

**Paramètres**
- **chip** : La puce dont le pourcentage d'échec sera renvoyé.

**Retour**
- **failure** : Pourcentage d'échec de la puce **chip**, un nombre entier entre **0** et **100**.

LeekScript : `getChipFailure()` — 15 opérations · https://leekwars.com/help/documentation/getChipFailure

### `Chip.features: list[Feature]`

Renvoie les effets de la puce **chip**.

**Paramètres**
- **chip** : La puce dont les effets seront renvoyés.

**Retour**
- **effects** : Les effets de la puce **chip**. Même valeur de retour que pour la fonction `getWeaponEffects`.

LeekScript : `getChipEffects()` — 125 opérations · https://leekwars.com/help/documentation/getChipEffects

### `Chip.bulbChips: list[Chip]`

Renvoie la liste des puces dont sera équipé le bulbe invoqué par la puce d'invocation **chip**.

Exemple :
```python
chips = Chip.punyBulb.bulbChips
Debug.log(chips)  # les puces que portera le bulbe
```

**Paramètres**
- **chip** : Identifiant d'une puce d'invocation (ex : `CHIP_PUNY_BULB`).

**Retour**
- **chips** : Une liste contenant les identifiants des puces du bulbe, ou `null` si **chip** n'est pas une puce d'invocation de bulbe.

LeekScript : `getBulbChips()` — 40 opérations · https://leekwars.com/help/documentation/getBulbChips

### `Chip.bulbCharacteristics: dict`

Pour une puce d'invocation : caractéristiques du bulbe invoqué (dict).

LeekScript : `getBulbCharacteristics()` — 40 opérations · https://leekwars.com/help/documentation/getBulbCharacteristics

### `Chip.bulbStats: dict`

Retourne les caractéristiques du bulbe invoqué par la puce **chip**.

Pour chaque caractéristique, l'intervalle de valeurs possibles est renvoyé sous la forme d'une liste `[min, max]`. Le bulbe créé prendra une valeur en suivant la formule `caracteristique = floor(min + (max - min) * min(300, niveauInvocateur) / 300)`.

Exemple :
```python
Debug.log(Chip.punyBulb.bulbStats)
# {1: [400, 500], 2: [50, 70], 3: [40, 60], ...}
```

**Paramètres**
- **chip** : Identifiant d'une puce d'invocation (ex : `CHIP_PUNY_BULB`).

**Retour**
- **stats** : Une Map associant chaque caractéristique (`STAT_LIFE`, `STAT_STRENGTH`, `STAT_AGILITY`, `STAT_WISDOM`, `STAT_RESISTANCE`, `STAT_SCIENCE`, `STAT_MAGIC`, `STAT_TP`, `STAT_MP`) à un intervalle `[min, max]` des valeurs possibles, ou `null` si **chip** n'est pas une puce d'invocation de bulbe.

LeekScript : `getBulbStats()` — 40 opérations · https://leekwars.com/help/documentation/getBulbStats

### `Chip.currentCooldownOf(entity: EntityLike) -> int`

Renvoie le cooldown actuel de la puce **chip** de l'entité **entity**.

Il s'agit du nombre de tours avant lesquels la puce deviendra utilisable, `0` si elle est actuellement utilisable. Pour les puces à cooldown infini comme `Régénération`, renvoie un nombre supérieur à `MAX_TURNS` après utilisation.

**Paramètres**
- **chip** : La puce dont le cooldown actuel sera renvoyé.
- **entity** : L'entité dont le cooldown sera renvoyé.

**Retour**
- **cooldown** : Le cooldown actuel de la puce **chip**.

LeekScript : `getCooldown()` — 30 opérations · https://leekwars.com/help/documentation/getCooldown

### `Chip.effectiveArea(cell: CellLike, frm: CellLike = ...) -> list[Cell]`

Renvoie la liste des cellules qui seront affectés si la puce **chip** est utilisée sur la cellule **cell** depuis une cellule **from**.
La fonction ne vérifie pas s'il est possible d'utiliser la puce sur la cellule **cell** ou de se rendre sur la cellule **from**.

**Paramètres**
- **chip** : La puce à tester.
- **cell** : La cellule cible.
- **from** : La cellule depuis laquelle la puce est utilisée.

**Retour**
- **cells** : Le tableau contenant toutes les cellules qui seront affectées.

LeekScript : `getChipEffectiveArea()` — 78 opérations · https://leekwars.com/help/documentation/getChipEffectiveArea

### `Chip.get(id: int) -> Chip`

La puce d'id `id`, ou None si l'id n'est pas celui d'une puce.

### `Chip.getAll() -> list[Chip]`

Retourne la liste de toutes les puces du jeu.

**Retour**
- **chips** : La liste de toutes les puces du jeu.

LeekScript : `getAllChips()` — 200 opérations · https://leekwars.com/help/documentation/getAllChips

### `Chip.isChip(value: Any) -> bool`

Détermine si une valeur est une constante représentant une puce.
```
isChip(CHIP_RAGE) = true;
isChip(WEAPON_PISTOL) = false.
```

**Paramètres**
- **value** : Le nombre à déterminer.

**Retour**
- **chip** : `true` si la valeur est une constante de puce, `false` sinon.

LeekScript : `isChip()` — 10 opérations · https://leekwars.com/help/documentation/isChip

## Effect

### `Effect.raw: list`

Tableau brut [type, value, caster_id, turns, critical, item_id, target_id, modifiers].

### `Effect.type: int`

### `Effect.value: int`

### `Effect.caster: Entity`

L'entité qui a lancé l'effet.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

### `Effect.turns: int`

### `Effect.critical: bool`

L'effet vient d'un coup critique.

### `Effect.item: Weapon | Chip`

L'arme ou la puce qui a provoqué l'effet (`Weapon`/`Chip`, comparable par `is`).

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

### `Effect.target: Entity`

L'entité qui subit l'effet.

⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).

### `Effect.modifiers: int`

### `Effect.getAll() -> list[int]`

Retourne la liste de tous les effets du jeu.

**Retour**
- **effects** : La liste de tous les effets du jeu.

LeekScript : `getAllEffects()` — 200 opérations · https://leekwars.com/help/documentation/getAllEffects

### `Effect.ABSOLUTE_SHIELD: int`

(= 6) Procure du bouclier absolu à une entité, permettant de réduire la quantité de points de vie retirée par les dégâts (EFFECT_DAMAGE) d'un montant fixe. Amplifié par la résistance.

LeekScript : `EFFECT_ABSOLUTE_SHIELD`

### `Effect.ABSOLUTE_VULNERABILITY: int`

(= 27) Retire du bouclier absolu à une entité. N'est pas amplifié par une caractéristique. Permet d'augmenter les points de vie retiré par les dégâts (EFFECT_DAMAGE) d'un montant absolu.

LeekScript : `EFFECT_ABSOLUTE_VULNERABILITY`

### `Effect.ADD_STATE: int`

(= 59)

LeekScript : `EFFECT_ADD_STATE`

### `Effect.AFTEREFFECT: int`

(= 25) Retire des points de vie à une entité. Amplifié par la science. Réduit le maximum de points de vie de 5% du montant de points de vie retiré.

LeekScript : `EFFECT_AFTEREFFECT`

### `Effect.ALLY_KILLED_TO_AGILITY: int`

(= 55)

LeekScript : `EFFECT_ALLY_KILLED_TO_AGILITY`

### `Effect.ANTIDOTE: int`

(= 23) Retire tous les poison (EFFECT_POISON) présent sur une cible.

LeekScript : `EFFECT_ANTIDOTE`

### `Effect.ATTRACT: int`

(= 46)

LeekScript : `EFFECT_ATTRACT`

### `Effect.BOOST_MAX_LIFE: int`

(= 12) Augmente les points de vie et le maximum de points de vie d'une entité. Amplifié par la sagesse.

LeekScript : `EFFECT_BOOST_MAX_LIFE`

### `Effect.BUFF_AGILITY: int`

(= 4) Procure de l'agilité à une entité. Amplifié par la science.

LeekScript : `EFFECT_BUFF_AGILITY`

### `Effect.BUFF_MP: int`

(= 7) Procure des points de mouvement à une entité. Amplifié par la science.

LeekScript : `EFFECT_BUFF_MP`

### `Effect.BUFF_RESISTANCE: int`

(= 21) Procure de la résistance à une entité. Amplifié par la science.

LeekScript : `EFFECT_BUFF_RESISTANCE`

### `Effect.BUFF_STRENGTH: int`

(= 3) Procure de la force à une entité. Amplifié par la science.

LeekScript : `EFFECT_BUFF_STRENGTH`

### `Effect.BUFF_TP: int`

(= 8) Procure des points d'action à une entité. Amplifié par la science.

LeekScript : `EFFECT_BUFF_TP`

### `Effect.BUFF_WISDOM: int`

(= 22) Procure de la sagesse à une entité. Amplifié par la science.

LeekScript : `EFFECT_BUFF_WISDOM`

### `Effect.CRITICAL_TO_HEAL: int`

(= 58)

LeekScript : `EFFECT_CRITICAL_TO_HEAL`

### `Effect.DAMAGE: int`

(= 1) Retire des points de vie à une entité. Amplifié par la force. Interagit avec les boucliers (EFFECT_ABSOLUTE_SHIELD, EFFECT_RELATIVE_SHIELD, EFFECT_VULNERABILITY, EFFECT_ABSOLUTE_VULNERABILITY), le vol de vie (à l'exception du lanceur), et le retour de dégâts (EFFECT_DAMAGE_RETURN). Réduit le maximum de points de vie de 5% du montant de points de vie retiré.

LeekScript : `EFFECT_DAMAGE`

### `Effect.DAMAGE_RETURN: int`

(= 20) Procure du renvoi de dégâts à une entité, permettant de retirer des points de vie aux entités infligeant des dégâts au bénéficiaire. Amplifié par l'agilité. Réduit le maximum de points de vie de 5% du montant de points de vie retiré.

LeekScript : `EFFECT_DAMAGE_RETURN`

### `Effect.DAMAGE_TO_ABSOLUTE_SHIELD: int`

(= 34)

LeekScript : `EFFECT_DAMAGE_TO_ABSOLUTE_SHIELD`

### `Effect.DAMAGE_TO_RESISTANCE: int`

(= 63)

LeekScript : `EFFECT_DAMAGE_TO_RESISTANCE`

### `Effect.DAMAGE_TO_STRENGTH: int`

(= 35)

LeekScript : `EFFECT_DAMAGE_TO_STRENGTH`

### `Effect.DEBUFF: int`

(= 9) Réduit la valeur de tous les effets présents sur une entité d'un pourcentage.

LeekScript : `EFFECT_DEBUFF`

### `Effect.HEAL: int`

(= 2) Rend des points de vie à une entité, limité par le maximum de points de vie. Amplifié par la sagesse.

LeekScript : `EFFECT_HEAL`

### `Effect.INVERT: int`

(= 11) Échange la position du lanceur avec celle d'une entité.

LeekScript : `EFFECT_INVERT`

### `Effect.KILL: int`

(= 16) Retire tous les points de vie d'une entité.

LeekScript : `EFFECT_KILL`

### `Effect.KILL_TO_TP: int`

(= 56)

LeekScript : `EFFECT_KILL_TO_TP`

### `Effect.LIFE_DAMAGE: int`

(= 28) Retire des points de vie à une entité, dépendant d'un pourcentage de la vie du lanceur. Interagit avec les boucliers (EFFECT_ABSOLUTE_SHIELD, EFFECT_RELATIVE_SHIELD, EFFECT_VULNERABILITY, EFFECT_ABSOLUTE_VULNERABILITY) et le retour de dégâts (EFFECT_DAMAGE_RETURN). Réduit le maximum de points de vie de 5% du montant de points de vie retiré.

LeekScript : `EFFECT_LIFE_DAMAGE`

### `Effect.MOVED_TO_MP: int`

(= 50)

LeekScript : `EFFECT_MOVED_TO_MP`

### `Effect.MULTIPLY_STATS: int`

(= 62)

LeekScript : `EFFECT_MULTIPLY_STATS`

### `Effect.NOVA_DAMAGE: int`

(= 30) Retire des points de vie max. Amplifié par la science.

LeekScript : `EFFECT_NOVA_DAMAGE`

### `Effect.NOVA_DAMAGE_TO_MAGIC: int`

(= 36)

LeekScript : `EFFECT_NOVA_DAMAGE_TO_MAGIC`

### `Effect.NOVA_VITALITY: int`

(= 45)

LeekScript : `EFFECT_NOVA_VITALITY`

### `Effect.POISON: int`

(= 13) Retire des points de vie à une entité. Amplifié par la magie. Réduit le maximum de points de vie de 10% du montant de points de vie retiré.

LeekScript : `EFFECT_POISON`

### `Effect.POISON_TO_SCIENCE: int`

(= 33)

LeekScript : `EFFECT_POISON_TO_SCIENCE`

### `Effect.PROPAGATION: int`

(= 43)

LeekScript : `EFFECT_PROPAGATION`

### `Effect.PUSH: int`

(= 51)

LeekScript : `EFFECT_PUSH`

### `Effect.RAW_ABSOLUTE_SHIELD: int`

(= 37) Procure du bouclier absolu à une entité, permettant de réduire la quantité de points de vie retirée par les dégâts (EFFECT_DAMAGE) d'un montant fixe. Non amplifiable.

LeekScript : `EFFECT_RAW_ABSOLUTE_SHIELD`

### `Effect.RAW_BUFF_AGILITY: int`

(= 41) Procure de l'agilité à une entité. Non amplifiable.

LeekScript : `EFFECT_RAW_BUFF_AGILITY`

### `Effect.RAW_BUFF_MAGIC: int`

(= 39) Procure de la magie à une entité. Non amplifiable.

LeekScript : `EFFECT_RAW_BUFF_MAGIC`

### `Effect.RAW_BUFF_MP: int`

(= 31) Procure des points de mouvement à une entité. Non amplifiable.

LeekScript : `EFFECT_RAW_BUFF_MP`

### `Effect.RAW_BUFF_POWER: int`

(= 52)

LeekScript : `EFFECT_RAW_BUFF_POWER`

### `Effect.RAW_BUFF_RESISTANCE: int`

(= 42)

LeekScript : `EFFECT_RAW_BUFF_RESISTANCE`

### `Effect.RAW_BUFF_SCIENCE: int`

(= 40) Procure de la science à une entité. Non amplifiable.

LeekScript : `EFFECT_RAW_BUFF_SCIENCE`

### `Effect.RAW_BUFF_STRENGTH: int`

(= 38) Procure de la force à une entité. Non amplifiable.

LeekScript : `EFFECT_RAW_BUFF_STRENGTH`

### `Effect.RAW_BUFF_TP: int`

(= 32) Procure des points d'action à une entité. Non amplifiable.

LeekScript : `EFFECT_RAW_BUFF_TP`

### `Effect.RAW_BUFF_WISDOM: int`

(= 44)

LeekScript : `EFFECT_RAW_BUFF_WISDOM`

### `Effect.RAW_HEAL: int`

(= 57)

LeekScript : `EFFECT_RAW_HEAL`

### `Effect.RAW_RELATIVE_SHIELD: int`

(= 54)

LeekScript : `EFFECT_RAW_RELATIVE_SHIELD`

### `Effect.RELATIVE_SHIELD: int`

(= 5) Procure un bouclier relatif, permettant de réduire la quantité de points de vie retiré par les dégâts (EFFECT_DAMAGE) d'un montant relatif. Amplifié par la résistance.

LeekScript : `EFFECT_RELATIVE_SHIELD`

### `Effect.REMOVE_SHACKLES: int`

(= 49)

LeekScript : `EFFECT_REMOVE_SHACKLES`

### `Effect.REPEL: int`

(= 53)

LeekScript : `EFFECT_REPEL`

### `Effect.RESURRECT: int`

(= 15) Ressuscite une entité, avec un nombre de PV maximum égal à la moitié du nombre de PV maximum de l'entité avant résurrection, et un nombre de PV courant égal au quart du nombre de PV maximum avant résurrection.

LeekScript : `EFFECT_RESURRECT`

### `Effect.SHACKLE_AGILITY: int`

(= 47)

LeekScript : `EFFECT_SHACKLE_AGILITY`

### `Effect.SHACKLE_MAGIC: int`

(= 24) Retire de la magie à une entité. Amplifié par la magie.

LeekScript : `EFFECT_SHACKLE_MAGIC`

### `Effect.SHACKLE_MP: int`

(= 17) Retire des points de mouvement à une entité. Amplifié par la magie.

LeekScript : `EFFECT_SHACKLE_MP`

### `Effect.SHACKLE_STRENGTH: int`

(= 19) Retire de la force à une entité. Amplifié par la magie.

LeekScript : `EFFECT_SHACKLE_STRENGTH`

### `Effect.SHACKLE_TP: int`

(= 18) Retire des points d'action à une entité. Amplifié par la magie.

LeekScript : `EFFECT_SHACKLE_TP`

### `Effect.SHACKLE_WISDOM: int`

(= 48)

LeekScript : `EFFECT_SHACKLE_WISDOM`

### `Effect.STEAL_ABSOLUTE_SHIELD: int`

(= 29)

LeekScript : `EFFECT_STEAL_ABSOLUTE_SHIELD`

### `Effect.STEAL_LIFE: int`

(= 61)

LeekScript : `EFFECT_STEAL_LIFE`

### `Effect.SUMMON: int`

(= 14) Invoque un bulbe. Aucun effet si la limite d'invocation de l'équipe est atteinte.

LeekScript : `EFFECT_SUMMON`

### `Effect.SUPERINFECTION: int`

(= 64) Fait détoner les poisons actifs de la cible : ils disparaissent tous et infligent d'un coup 50% de la somme de leurs valeurs (65% en critique). Les tours qu'il leur restait à courir n'entrent pas dans le calcul. Les poisons infinis ne détonent pas.

LeekScript : `EFFECT_SUPERINFECTION`

### `Effect.TELEPORT: int`

(= 10) Change la position du lanceur.

LeekScript : `EFFECT_TELEPORT`

### `Effect.TOTAL_DEBUFF: int`

(= 60)

LeekScript : `EFFECT_TOTAL_DEBUFF`

### `Effect.VULNERABILITY: int`

(= 26) Retire du bouclier relatif à une entité. N'est pas amplifié par une caractéristique. Permet d'augmenter les points de vie retiré par les dégâts (EFFECT_DAMAGE) d'un montant relatif.

LeekScript : `EFFECT_VULNERABILITY`

## Feature

### `Feature.raw: list`

Tableau brut [type, minValue, maxValue, turns, targets, modifiers].

### `Feature.type: int`

### `Feature.minValue: int`

### `Feature.maxValue: int`

### `Feature.turns: int`

### `Feature.targets: int`

### `Feature.modifiers: int`

## State

### `State.INVINCIBLE: int`

(= 3)

LeekScript : `STATE_INVINCIBLE`

### `State.PACIFIST: int`

(= 4)

LeekScript : `STATE_PACIFIST`

### `State.ROOTED: int`

(= 9) Désigne l'état Enraciné : l'entité ne peut plus se déplacer, ni être poussée ou attirée, mais l'Inversion et le Rempotage la déplacent toujours.

LeekScript : `STATE_ROOTED`

### `State.STATIC: int`

(= 11)

LeekScript : `STATE_STATIC`

### `State.STERILE: int`

(= 12)

LeekScript : `STATE_STERILE`

### `State.UNHEALABLE: int`

(= 2) Désigne l'état Insoignable : l'entité ne peut plus être soignée — soins, vol de vie et régénération n'ont aucun effet sur elle.

LeekScript : `STATE_UNHEALABLE`

## Registers

### `Registers.get(key: str) -> str`

Renvoie la valeur stockée dans le registre de l'entité associé à la clé **key** ou null si le registre n'existe pas.

**Paramètres**
- **key** : La clé du registre dont la valeur sera retournée.

**Retour**
- **value** : La valeur stockée dans le registre de clé **key**.

LeekScript : `getRegister()` — 15 opérations · https://leekwars.com/help/documentation/getRegister

### `Registers.set(key: str, value: Any) -> bool`

Stocke la valeur **value** dans le registre de clé **key**.
La clé et la valeur sont des chaînes qui doivent contenir respectivement *100* et *5000* caractères au maximum. Un poireau peut posséder au maximum *100* registres, le stockage dans un nouveau registre ne fonctionnera pas si tous les registres
sont déjà occupés.

**Paramètres**
- **key** : La clé du registre où stocker la valeur.
- **value** : La valeur à stocker.

**Retour**
- **success** : `true` si l'opération s'est bien passée, `false` sinon.

LeekScript : `setRegister()` — 50 opérations · https://leekwars.com/help/documentation/setRegister

### `Registers.delete(key: str) -> None`

Supprime le registre associé à la clé **key** s'il existe.

**Paramètres**
- **key** : La clé du registre à supprimer.

LeekScript : `deleteRegister()` — 16 opérations · https://leekwars.com/help/documentation/deleteRegister

### `Registers.all() -> dict[str, str]`

Renvoie l'ensemble des registres de l'entité sous la forme d'un tableau associatif [*clé du registre* : *valeur du registre*]. Exemple : 
```
debug(getRegisters());
// Affiche par exemple :
// ['reg1' : '314323', 'reg2' : 'test_string']
```

**Retour**
- **registers** : Le tableau associatif correspondant à tous les registres de l'entité.

LeekScript : `getRegisters()` — 25 opérations · https://leekwars.com/help/documentation/getRegisters

## Network

### `Network.sendTo(entity: EntityLike, type: int, params: Any) -> bool`

Envoie un message à l'entité d'id **entity**.

**Paramètres**
- **entity** : L'id de l'entité auquelle sera envoyé le message.
- **type** : Le type du message à envoyer (voir les constantes MESSAGE_*).
- **params** : Les paramètres du message, qui peuvent être n'importe quelle valeur.

**Retour**
- **sent** : `true` si l'envoi a été effectué, `false` si une erreur est survenue.

LeekScript : `sendTo()` — 15 opérations · https://leekwars.com/help/documentation/sendTo

### `Network.sendAll(type: int, params: Any) -> None`

Envoie un message à toute votre équipe.

**Paramètres**
- **type** : Le type du message à envoyer (voir les constantes MESSAGE_*).
- **params** : Les paramètres du message, qui peuvent être n'importe quelle valeur.

LeekScript : `sendAll()` — 40 opérations · https://leekwars.com/help/documentation/sendAll

### `Network.getMessages(entity: EntityLike = ...) -> list[Message]`

Renvoie le tableau des messages de l'entité **entity**.

**Paramètres**
- **entity** : L'entité dont les messages seront renvoyés.

**Retour**
- **messages** : Le tableau des messages reçus par **entity**.
	Un message est représenté lui-même sous la forme d'un tableau de la forme : [**auteur**, **type**, **paramètres**]

	Les différents types de messages sont représentés par les constantes :

	- `MESSAGE_HEAL` : demande de soins
	- `MESSAGE_ATTACK` : demande d'attaquer
	- `MESSAGE_BUFF_STRENGTH` : demande de boost force
	- ...

**Informations supplémentaires**
- Il est possible de lire les messages envoyés entre deux autres entités si notre tour de jeu se situe entre l'entité l'entité qui émet et celle qui reçoit le message. Les messages addressés à une entité sont supprimés à la fin de son tour de jeu.
- Les messages envoyés par les entités de type `ENTITY_MOB` (dans les combats de boss) ne sont pas visibles par les poireaux.

LeekScript : `getMessages()` — -1 opérations · https://leekwars.com/help/documentation/getMessages

## Message

### `Message.raw: list`

Message brut tel que renvoyé par getMessages().

### `Message.author: Entity`

Renvoie l'entité auteur du message **message**.

**Paramètres**
- **message** : Le message dont l'auteur sera renvoyé.

**Retour**
- **entity** : L'entité auteur du message **message**.

LeekScript : `getMessageAuthor()` — 5 opérations · https://leekwars.com/help/documentation/getMessageAuthor

### `Message.type: int`

Renvoie le type du message **message**.

**Paramètres**
- **message** : Le message dont le type sera renvoyé (parmis `MESSAGE_HEAL`, `MESSAGE_ATTACK`, etc.).

**Retour**
- **type** : Le type du message **message**.

LeekScript : `getMessageType()` — 5 opérations · https://leekwars.com/help/documentation/getMessageType

### `Message.params: Any`

Renvoie le tableau des paramètres du message **message**.

**Paramètres**
- **message** : Le message dont les paramètres seront renvoyés.

**Retour**
- **params** : Les paramètres du message **message**.

LeekScript : `getMessageParams()` — 5 opérations · https://leekwars.com/help/documentation/getMessageParams

## Debug

### `Debug.log(value: Any, color: int = ...) -> None`

Enregistre un message **object** dans le log personnel, disponible dans le rapport à la fin du combat.

La limite sur la quantité de `debug()` possible par combat est de **500 000** caractères.

*Exemple*:
```python
Debug.log(f"Ma variable degats vaut : {degats}")
```

**Paramètres**
- **object** : Le message à enregistrer.

LeekScript : `debug()` — 100 opérations · https://leekwars.com/help/documentation/debug

### `Debug.mark(cells: Any, color: int = ..., duration: int = ...) -> bool`

Marque une ou plusieurs cellules de la couleur indiquée en paramètre sur le terrain pour le nombre de tour indiqué en paramètre. Ce marquage n'est visible que par l'éleveur de l'entité.

**Paramètres**
- **cells** : La cellule ou tableau de plusieurs cellules à marquer
- **color** : Couleur du marquage
- **duration** : Durée du marquage

**Retour**
- **success** : Retourne true si tout s'est bien déroulé

LeekScript : `mark()` — 164 opérations · https://leekwars.com/help/documentation/mark

### `Debug.markText(cells: Any, text: Any, color: int = ..., duration: int = ...) -> bool`

Écrit un texte sur une ou plusieurs cellules de la couleur indiquée en paramètre sur le terrain pour le nombre de tour indiqué en paramètre. Ces textes ne sont visibles que par l'éleveur de l'entité.

**Paramètres**
- **cells** : La cellule ou tableau de plusieurs cellules où écrire
- **text** : Le texte à écrire (maximum 10 caractères)
- **color** : Couleur du texte
- **duration** : Durée du texte

**Retour**
- **success** : Retourne true si tout s'est bien déroulé

LeekScript : `markText()` — 164 opérations · https://leekwars.com/help/documentation/markText

### `Debug.clearMarks() -> None`

Efface tous les marquages effectués par `mark` et `markText` sur le terrain.

LeekScript : `clearMarks()` — 15 opérations · https://leekwars.com/help/documentation/clearMarks

### `Debug.show(cell: CellLike, color: int = ...) -> bool`

Montre aux joueurs une cellule **cell** de la couleur **color** sur le terrain pour 1 tour.

Cette fonction coûte **1PT** .

La limite de show() par tour est de **5**.

**Paramètres**
- **cell** : La cellule à montrer
- **color** : Couleur du marquage (par défaut gris foncé)

LeekScript : `show()` — 8 opérations · https://leekwars.com/help/documentation/show

### `Debug.pause() -> None`

Met en pause le combat, uniquement pour l'éleveur de l'entité qui utilise la fonction.

LeekScript : `pause()` — 30 opérations · https://leekwars.com/help/documentation/pause

## System

### `System.operations: int`

Renvoie le nombre d'opérations consommées par votre entité depuis le début de son tour. Ce nombre doit rester inférieur à `getMaxOperations` pour ne pas que l'entité plante.

*Exemple* :
```python
if System.operations > System.maxOperations * 0.9:
	break  # 90% des opérations utilisées, on arrête.
```

**Retour**
- **operations** : Nombre d'opérations consommées par votre entité depuis le début de son tour.

LeekScript : `getOperations()` — 1 opérations · https://leekwars.com/help/documentation/getOperations

### `System.maxOperations: int`

Retourne le nombre maximal d'opérations utilisable votre l'entité.

**Retour**
- **operations** : Votre nombre maximal d'opérations.

LeekScript : `getMaxOperations()` — 1 opérations · https://leekwars.com/help/documentation/getMaxOperations

### `System.instructionsCount: int`

Renvoie le nombre d'instructions que votre entité a effectué durant le tour actuel.

**Retour**
- **instructions** : Le nombre d'instructions que votre entité a effectué durant le tour actuel.

LeekScript : `getInstructionsCount()` — 1 opérations · https://leekwars.com/help/documentation/getInstructionsCount

### `System.usedRAM: int`

Renvoie la quantité de RAM acteullement utilisée par votre IA.

**Retour**
- **ram** : La RAM utilisée actuellement.

LeekScript : `getUsedRAM()` — 1 opérations · https://leekwars.com/help/documentation/getUsedRAM

### `System.maxRAM: int`

Renvoie la limite utilisable de RAM de votre IA. La RAM est consommée en créant des listes, des tables et des objets.

La limite actuelle est de 100 mégaoctets soit 12 500 000 éléments de liste.

**Retour**
- **ram** : La limite de RAM.

LeekScript : `getMaxRAM()` — 1 opérations · https://leekwars.com/help/documentation/getMaxRAM

### `System.date: str`

Renvoie la date du combat, au format `dd/MM/yyyy`.

**Retour**
- **date** : La date du combat.

LeekScript : `getDate()` — 50 opérations · https://leekwars.com/help/documentation/getDate

### `System.time: str`

Renvoie le temps du début du combat, au format `HH:mm:ss`.

**Retour**
- **time** : Le temps du combat.

**Exemples**
```python
time = System.time
Debug.log(f"Temps du combat : {time}")
```

LeekScript : `getTime()` — 50 opérations · https://leekwars.com/help/documentation/getTime

### `System.timestamp: int`

Renvoie l'horodatage du combat, égal au nombre de secondes depuis le 1er janvier 1970 (temps Unix).

**Retour**
- **timestamp** : L'horodatage du combat.

**Exemples**
```python
timestamp = System.timestamp
Debug.log(f"Horodatage du combat : {timestamp}")
```

LeekScript : `getTimestamp()` — 5 opérations · https://leekwars.com/help/documentation/getTimestamp

## Color

### `Color.rgb(r: int, g: int, b: int) -> int`

Retourne l'entier correspondant à la couleur (**red**, **green**, **blue**) fournie en paramètres.

**Paramètres**
- **red** : Valeur du rouge entre 0 et 255.
- **green** : Valeur du vert entre 0 et 255.
- **blue** : Valeur du bleu entre 0 et 255.

**Retour**
- **color** : int correspondant à la couleur fournie en paramètre.

LeekScript : `getColor()` — 7 opérations · https://leekwars.com/help/documentation/getColor

### `Color.red(color: int) -> int`

Renvoie le taux de rouge dans la couleur **color**, entre 0 et 255. Par exemple, `getRed(COLOR_RED) = 255` et `getRed(COLOR_BLUE) = 0`.

**Paramètres**
- **color** : La couleur dont le taux de rouge sera renvoyé.

**Retour**
- **red** : Le taux de rouge dans la couleur **color**

LeekScript : `getRed()` — 2 opérations · https://leekwars.com/help/documentation/getRed

### `Color.green(color: int) -> int`

Renvoie le taux de vert dans la couleur **color**, entre 0 et 255. Par exemple, `getGreen(COLOR_GREEN) = 255` et `getGreen(COLOR_RED) = 0`.

**Paramètres**
- **color** : La couleur dont le taux de vert sera renvoyé.

**Retour**
- **green** : Le taux de vert dans la couleur **color**

LeekScript : `getGreen()` — 2 opérations · https://leekwars.com/help/documentation/getGreen

### `Color.blue(color: int) -> int`

Renvoie le taux de bleu dans la couleur **color**, entre 0 et 255.

Par exemple, getBlue(`COLOR_BLUE`) = 255 et getBlue(`COLOR_GREEN`) = 0.

**Paramètres**
- **color** : La couleur dont le taux de bleu sera renvoyé.

**Retour**
- **blue** : Le taux de bleu dans la couleur **color**

LeekScript : `getBlue()` — 1 opérations · https://leekwars.com/help/documentation/getBlue

### `Color.BLUE: int`

(= 255) Couleur bleue.

LeekScript : `COLOR_BLUE`

### `Color.GREEN: int`

(= 65280) Couleur verte.

LeekScript : `COLOR_GREEN`

### `Color.RED: int`

(= 16711680) Couleur rouge.

LeekScript : `COLOR_RED`

## Math

### `Math.isPermutation(a: int, b: int) -> bool`

Renvoie *true* si les nombres **x** et **y** sont des permutations dans leur représentation décimale, *false* sinon.

**Paramètres**
- **x** : Premier nombre.
- **y** : Second nombre.

**Retour**
- **permutation** : *true* si les nombres **x** et **y** sont des permutations, *false* sinon.

**Exemples**
```python
Math.isPermutation(1234, 4321)         # True
Math.isPermutation(12345678, 51762384) # True
Math.isPermutation(11112222, 22221111) # True
Math.isPermutation(123456, 12345678)   # False
```

LeekScript : `isPermutation()` — 10 opérations · https://leekwars.com/help/documentation/isPermutation

### `Math.signum(x: float) -> int`

Détermine le signe du nombre **number**.

**Paramètres**
- **number** Le nombre dont le signe sera déterminé.

**Retour**
- **sign** 1 si le nombre est positif, 0 si le nombre est nul et -1 si le nombre est négatif.

**Exemples**
`signum(0) // 0`
`signum(50) // 1`
`signum(-12) // -1`

LeekScript : `signum()` — 1 opérations · https://leekwars.com/help/documentation/signum

### `Math.setBit(x: int, bit: int, value: bool = True) -> int`

Renvoie le nombre **number** dont le bit situé à la position **position** a été mis à la valeur **value** (`1` par défaut). Le nombre d'origine n'est pas modifié.

La position `0` désigne le bit de poids faible. La fonction fonctionne aussi sur les grands entiers.

Exemple :
```python
Math.setBit(0, 3)      # 8  : met le bit 3 à 1   (1000 en binaire)
Math.setBit(15, 1, False)  # 13 : met le bit 1 à 0 (1101 en binaire)
```

**Paramètres**
- **number** : Nombre entier de départ.
- **position** : Position du bit à modifier, `0` étant le bit de poids faible.
- **value** *(optionnel)* : Nouvelle valeur du bit : `1`/`true` pour l'activer, `0`/`false` pour le désactiver. Vaut `1` par défaut.

**Retour**
- **result** : Le nombre **number** avec le bit modifié.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `testBit` et `bitLength`.

LeekScript : `setBit()` — 1 opérations · https://leekwars.com/help/documentation/setBit

### `Math.testBit(x: int, bit: int) -> bool`

Renvoie `true` si le bit situé à la position **bit** du nombre **x** vaut `1`, et `false` sinon. La position `0` désigne le bit de poids faible. La fonction fonctionne aussi sur les grands entiers.

```python
Math.testBit(8, 3)  # True  : 8 = 1000, bit 3 à 1
Math.testBit(8, 0)  # False : bit 0 à 0
Math.testBit(13, 2) # True  : 13 = 1101, bit 2 à 1
```

**Paramètres**
- **x** : Le nombre entier à tester.
- **bit** : La position du bit à tester, `0` étant le bit de poids faible.

**Retour**
- **set** : `true` si le bit à la position **bit** vaut `1`, `false` sinon.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `setBit`, `bitLength` et `bitCount`.

LeekScript : `testBit()` — 1 opérations · https://leekwars.com/help/documentation/testBit

### `Math.bitReverse(x: int) -> int`

Renvoie le nombre obtenu en inversant l'ordre des 64 bits de l'entier **x** : le bit de poids faible (position `0`) devient le bit de poids fort (position `63`), et ainsi de suite. Le nombre d'origine n'est pas modifié.

L'inversion porte toujours sur les 64 bits, y compris les zéros de tête : `bitReverse(12)` (`1100` en binaire) place ces quatre bits tout en haut de l'entier et renvoie `3458764513820540928`, soit `0011` suivi de 60 zéros. Comme le bit `0` arrive en position `63`, celle du signe, le résultat est négatif dès que **x** est impair.

```python
Math.bitReverse(0)   # 0
Math.bitReverse(12)  # 3458764513820540928 : 1100 devient 0011 suivi de 60 zéros
Math.bitReverse(1)   # -9223372036854775808 : le bit 0 devient le bit de signe
```

**Paramètres**
- **x** : L'entier 64 bits dont les bits seront inversés.

**Retour**
- **reversed** : Le nombre dont les bits sont ceux de **x** dans l'ordre inverse.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `byteReverse`, `rotateLeft` et `binString`.

LeekScript : `bitReverse()` — 1 opérations · https://leekwars.com/help/documentation/bitReverse

### `Math.byteReverse(x: int) -> int`

Renvoie le nombre obtenu en inversant l'ordre des 8 octets de l'entier 64 bits **x** : l'octet de poids faible devient l'octet de poids fort, et ainsi de suite. Les bits à l'intérieur de chaque octet ne bougent pas. Le nombre d'origine n'est pas modifié.

C'est l'opération de changement de boutisme (*endianness*). L'inversion porte toujours sur les 8 octets, y compris les octets nuls de tête : `byteReverse(1)` renvoie `72057594037927936`, soit `1` suivi de 56 zéros en binaire.

```python
Math.byteReverse(0)  # 0
Math.byteReverse(1)  # 72057594037927936 : l'octet 01 passe tout en haut
hex(Math.byteReverse(0x0102))  # '0x201000000000000'
```

**Paramètres**
- **x** : L'entier 64 bits dont les octets seront inversés.

**Retour**
- **reversed** : Le nombre dont les octets sont ceux de **x** dans l'ordre inverse.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `bitReverse` et `hexString`.

LeekScript : `byteReverse()` — 1 opérations · https://leekwars.com/help/documentation/byteReverse

### `Math.rotateLeft(x: int, count: int) -> int`

Renvoie le nombre obtenu en faisant tourner les 64 bits de l'entier **x** de **s** positions vers la gauche : les bits qui sortent par le haut rentrent par le bas. Contrairement au décalage `<<`, aucun bit n'est perdu. Le nombre d'origine n'est pas modifié.

La rotation porte sur les 64 bits, bit de signe compris. Une rotation de `64` positions redonne **x**, et une valeur de **s** négative tourne vers la droite : `rotateLeft(x, -s)` équivaut à `rotateRight``(x, s)`.

```python
Math.rotateLeft(1, 1)   # 2
Math.rotateLeft(11, 2)  # 44 : 1011 devient 101100
Math.rotateLeft(1, 63)  # -9223372036854775808 : le bit 0 arrive sur le bit de signe
Math.rotateLeft(1, 64)  # 1 : tour complet
```

**Paramètres**
- **x** : L'entier 64 bits à faire tourner.
- **s** : Le nombre de positions de la rotation. Négatif pour tourner vers la droite.

**Retour**
- **rotated** : Le nombre **x** après rotation de **s** bits vers la gauche.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `rotateRight` et `bitReverse`.

LeekScript : `rotateLeft()` — 1 opérations · https://leekwars.com/help/documentation/rotateLeft

### `Math.rotateRight(x: int, count: int) -> int`

Renvoie le nombre obtenu en faisant tourner les 64 bits de l'entier **x** de **s** positions vers la droite : les bits qui sortent par le bas rentrent par le haut. Contrairement au décalage `>>`, aucun bit n'est perdu. Le nombre d'origine n'est pas modifié.

La rotation porte sur les 64 bits, bit de signe compris : `rotateRight(1, 1)` envoie le bit `0` en position `63` et renvoie donc un nombre négatif. Une rotation de `64` positions redonne **x**, et une valeur de **s** négative tourne vers la gauche : `rotateRight(x, -s)` équivaut à `rotateLeft``(x, s)`.

```python
Math.rotateRight(2, 1)   # 1
Math.rotateRight(44, 2)  # 11 : 101100 devient 1011
Math.rotateRight(1, 1)   # -9223372036854775808 : le bit 0 arrive sur le bit de signe
Math.rotateRight(1, 64)  # 1 : tour complet
```

**Paramètres**
- **x** : L'entier 64 bits à faire tourner.
- **s** : Le nombre de positions de la rotation. Négatif pour tourner vers la gauche.

**Retour**
- **rotated** : Le nombre **x** après rotation de **s** bits vers la droite.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `rotateLeft` et `bitReverse`.

LeekScript : `rotateRight()` — 1 opérations · https://leekwars.com/help/documentation/rotateRight

### `Math.leadingZeros(x: int) -> int`

Renvoie le nombre de bits à `0` en tête de l'entier **x**, c'est-à-dire avant son premier bit à `1` en partant du bit de poids fort. Le compte se fait toujours sur les 64 bits d'un entier signé : `leadingZeros(8)` renvoie `60`, car `8` s'écrit `1000` et occupe les 4 bits de poids faible sur les 64.

Renvoie `64` lorsque **x** vaut `0`, et `0` lorsque **x** est négatif, puisque son bit de signe est à `1`. Pour un nombre positif, `leadingZeros(x) + bitLength(x)` vaut toujours `64`.

```python
Math.leadingZeros(0)    # 64 : aucun bit à 1
Math.leadingZeros(1)    # 63
Math.leadingZeros(8)    # 60 : 1000 en binaire
Math.leadingZeros(255)  # 56 : 11111111 en binaire
```

**Paramètres**
- **x** : L'entier 64 bits dont les zéros de tête seront comptés.

**Retour**
- **zeros** : Le nombre de zéros de tête de **x**, entre `0` et `64`.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `trailingZeros`, `bitLength` et `bitCount`.

LeekScript : `leadingZeros()` — 1 opérations · https://leekwars.com/help/documentation/leadingZeros

### `Math.trailingZeros(x: int) -> int`

Renvoie le nombre de bits à `0` en queue de l'entier **x**, c'est-à-dire avant son premier bit à `1` en partant du bit de poids faible. C'est la position du bit à `1` le plus bas, ou encore l'exposant de la plus grande puissance de `2` qui divise **x**.

Renvoie `64` lorsque **x** vaut `0`, puisque aucun bit n'est à `1`. La fonction fonctionne aussi sur les grands entiers.

```python
Math.trailingZeros(0)   # 64 : aucun bit à 1
Math.trailingZeros(1)   # 0
Math.trailingZeros(8)   # 3  : 1000 en binaire
Math.trailingZeros(12)  # 2  : 1100 en binaire
```

**Paramètres**
- **x** : L'entier dont les zéros de queue seront comptés.

**Retour**
- **zeros** : Le nombre de zéros de queue de **x**, entre `0` et `64`.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `leadingZeros`, `bitLength` et `bitCount`.

LeekScript : `trailingZeros()` — 1 opérations · https://leekwars.com/help/documentation/trailingZeros

### `Math.realBits(x: float) -> int`

Renvoie la représentation interne du nombre réel **x** sous forme d'entier : les 64 bits du réel au format IEEE 754 (double précision), lus tels quels comme un entier 64 bits signé. Le signe, l'exposant et la mantisse se retrouvent donc dans l'entier renvoyé.

Attention, ce n'est **pas** l'écriture binaire de **x** : `realBits(12)` ne renvoie pas `1100` mais `4622945017495814144`, car ce sont les bits du réel `12.0` qui sont lus. Pour obtenir l'écriture binaire d'un entier, utilisez `binString`.

La fonction inverse est `bitsToReal` : `bitsToReal(realBits(x))` redonne exactement **x**.

```python
Math.realBits(0.0)   # 0
Math.realBits(1.0)   # 4607182418800017408
Math.realBits(2.0)   # 4611686018427387904
Math.realBits(-1.0)  # -4616189618054758400 : le bit de signe est à 1
```

**Paramètres**
- **x** : Le nombre réel dont les bits seront renvoyés.

**Retour**
- **bits** : Les 64 bits IEEE 754 de **x**, sous forme d'entier signé.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `bitsToReal`, `binString` et `hexString`.

LeekScript : `realBits()` — 1 opérations · https://leekwars.com/help/documentation/realBits

### `Math.bitsToReal(bits: int) -> float`

Renvoie le nombre réel dont la représentation interne est l'entier **x** : les 64 bits de **x** sont lus tels quels comme un réel au format IEEE 754 (double précision). C'est la fonction inverse de `realBits`.

Attention, la fonction ne lit **pas** **x** comme une écriture binaire : `bitsToReal(10110)` ne renvoie pas `22` mais `4.995e-320`, un nombre dénormalisé minuscule, car l'entier `10110` n'a que quelques bits de poids faible à `1`. Pour écrire un nombre en binaire, utilisez le littéral `0b10110`.

```python
Math.bitsToReal(0)                    # 0.0
Math.bitsToReal(4607182418800017408)  # 1.0
Math.bitsToReal(4611686018427387904)  # 2.0
Math.bitsToReal(1)                    # 4.9e-324 : le plus petit réel positif
```

**Paramètres**
- **x** : L'entier 64 bits à lire comme un réel IEEE 754.

**Retour**
- **real** : Le réel dont les bits sont ceux de **x**.

**Note**
- Disponible à partir du `LeekScript 4`. Voir aussi `realBits`.

LeekScript : `bitsToReal()` — 3 opérations · https://leekwars.com/help/documentation/bitsToReal

## Armes

- `Weapon.pistol` — **Pistolet** (`weapon_pistol`, id 1, niveau 1) 3 PT, portée 1–7, zone POINT, lancer CIRCLE, 4 util./tour. Effets : Effect.DAMAGE 15–20.
- `Weapon.machineGun` — **Machine gun** (`weapon_machine_gun`, id 2, niveau 8) 4 PT, portée 1–6, zone POINT, lancer LINE, 3 util./tour. Effets : Effect.DAMAGE 10–15 ; Effect.DAMAGE 10–15 ; Effect.DAMAGE 10–15.
- `Weapon.neutrino` — **Neutrino** (`weapon_neutrino`, id 27, niveau 12) 4 PT, portée 2–6, zone POINT, lancer DIAGONAL, 3 util./tour. Effets : Effect.DAMAGE 25–30 ; Effect.VULNERABILITY 8 (2 tours).
- `Weapon.shotgun` — **Fusil à pompe** (`weapon_shotgun`, id 4, niveau 16) 5 PT, portée 1–5, zone POINT, lancer LINE, 2 util./tour. Effets : Effect.DAMAGE 33–43 ; Effect.ABSOLUTE_VULNERABILITY 25 (1 tours).
- `Weapon.magnum` — **Magnum** (`weapon_magnum`, id 5, niveau 27) 5 PT, portée 1–8, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 25–40.
- `Weapon.broadsword` — **Glaive** (`weapon_broadsword`, id 15, niveau 30) 5 PT, portée 1, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 39–41 ; Effect.RAW_BUFF_STRENGTH 40 (2 tours).
- `Weapon.laser` — **Laser** (`weapon_laser`, id 6, niveau 38) 6 PT, portée 2–9, zone LASER_LINE, lancer LINE, 2 util./tour. Effets : Effect.DAMAGE 43–59.
- `Weapon.doubleGun` — **Double gun** (`weapon_double_gun`, id 3, niveau 45) 4 PT, portée 2–7, zone POINT, lancer CIRCLE, 3 util./tour. Effets : Effect.DAMAGE 18–25 ; Effect.POISON 9–12 (2 tours).
- `Weapon.odachi` — **Odachi** (`weapon_odachi`, id 37, niveau 50) 9 PT, portée 1, zone POINT, lancer CIRCLE, 1 util./tour. Effets : Effect.DAMAGE 100–120.
- `Weapon.sword` — **Épée** (`weapon_sword`, id 35, niveau 75) 6 PT, portée 1, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 50–60 ; Effect.RAW_RELATIVE_SHIELD 8 (2 tours).
- `Weapon.destroyer` — **Destroyer** (`weapon_destroyer`, id 9, niveau 85) 6 PT, portée 1–6, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 40–60 ; Effect.SHACKLE_STRENGTH 17 (2 tours).
- `Weapon.unstableDestroyer` — **Destroyer instable** (`weapon_unstable_destroyer`, id 34, niveau 86) 6 PT, portée 1–6, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 10–90. Passifs : Effect.CRITICAL_TO_HEAL 50–150.
- `Weapon.flameThrower` — **Lance-flammes** (`weapon_flame_thrower`, id 8, niveau 90) 6 PT, portée 2–8, zone LASER_LINE, lancer LINE, 2 util./tour. Effets : Effect.DAMAGE 35–40 ; Effect.POISON 24–30 (2 tours).
- `Weapon.bLaser` — **B-Laser** (`weapon_b_laser`, id 13, niveau 95) 5 PT, portée 2–8, zone LASER_LINE, lancer LINE, 3 util./tour. Effets : Effect.DAMAGE 50–60 ; Effect.HEAL 50–60.
- `Weapon.excalibur` — **Excalibur** (`weapon_excalibur`, id 38, niveau 100) 12 PT, portée 1, zone POINT, lancer CIRCLE, 1 util./tour. Effets : Effect.DAMAGE 150–170 ; Effect.POISON 150–170 (2 tours).
- `Weapon.axe` — **Hache** (`weapon_axe`, id 16, niveau 110) 6 PT, portée 1, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 55–77 ; Effect.SHACKLE_MP 0.7–0.8 (1 tours).
- `Weapon.grenadeLauncher` — **Lance-grenades** (`weapon_grenade_launcher`, id 7, niveau 135) 6 PT, portée 4–7, zone CIRCLE_2, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 55–63.
- `Weapon.illicitGrenadeLauncher` — **Lance-grenades illicite** (`weapon_illicit_grenade_launcher`, id 18, niveau 136) 6 PT, portée 4–7, zone CIRCLE_2, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 10 ; Effect.DAMAGE 10 ; Effect.DAMAGE 10 ; Effect.DAMAGE 10. Passifs : Effect.POISON_TO_SCIENCE 10.
- `Weapon.desertSaber` — **Sabre du désert** (`weapon_desert_saber`, id 41, niveau 151) 6 PT, portée 1, zone POINT, lancer CIRCLE, 1 util./tour. Effets : Effect.DAMAGE 75–85 ; Effect.ADD_STATE 12 (2 tours).
- `Weapon.jLaser` — **J-Laser** (`weapon_j_laser`, id 17, niveau 153) 5 PT, portée 5–11, zone LASER_LINE, lancer LINE, 3 util./tour. Effets : Effect.ABSOLUTE_VULNERABILITY 25 (2 tours) ; Effect.STEAL_ABSOLUTE_SHIELD 25 (2 tours).
- `Weapon.bazooka` — **Bazooka** (`weapon_bazooka`, id 29, niveau 168) 11 PT, portée 8–12, zone CIRCLE_3, lancer DIAGONAL, 1 util./tour. Effets : Effect.DAMAGE 110–118.
- `Weapon.plutoniumBazooka` — **Bazooka au plutonium** (`weapon_plutonium_bazooka`, id 26, niveau 169) 11 PT, portée 8–12, zone CIRCLE_3, lancer DIAGONAL, 1 util./tour. Effets : Effect.SHACKLE_TP 1–1.3 (2 tours). Passifs : Effect.DAMAGE_TO_RESISTANCE 5.
- `Weapon.rhino` — **Rhino** (`weapon_rhino`, id 23, niveau 187) 5 PT, portée 2–4, zone POINT, lancer CIRCLE, 3 util./tour. Effets : Effect.DAMAGE 54–60.
- `Weapon.scythe` — **Faux** (`weapon_scythe`, id 39, niveau 200) 15 PT, portée 1, zone POINT, lancer CIRCLE, 1 util./tour. Effets : Effect.DAMAGE 300–350.
- `Weapon.sunSpear` — **Lance du soleil** (`weapon_sun_spear`, id 42, niveau 201) 7 PT, portée 1–4, zone LASER_LINE, lancer LINE, 1 util./tour. Effets : Effect.DAMAGE 75–90 ; Effect.REPEL 4.
- `Weapon.electrisor` — **Électriseur** (`weapon_electrisor`, id 11, niveau 211) 7 PT, portée 7, zone PLUS_1, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 70–80.
- `Weapon.mysteriousElectrisor` — **Électriseur mystérieux** (`weapon_mysterious_electrisor`, id 19, niveau 212) 7 PT, portée 7, zone PLUS_1, lancer CIRCLE, 2 util./tour. Effets : Effect.NOVA_DAMAGE 34–40 ; Effect.VULNERABILITY 7 (2 tours). Passifs : Effect.DAMAGE_TO_ABSOLUTE_SHIELD 4.
- `Weapon.lightninger` — **Foudroyeur** (`weapon_lightninger`, id 25, niveau 237) 9 PT, portée 6–10, zone X_1, lancer STAR, 2 util./tour. Effets : Effect.DAMAGE 99–107.
- `Weapon.enhancedLightninger` — **Foudroyeur amélioré** (`weapon_enhanced_lightninger`, id 33, niveau 238) 9 PT, portée 6–10, zone SQUARE_1, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 89–93 ; Effect.RAW_HEAL 100. Passifs : Effect.KILL_TO_TP 1.
- `Weapon.katana` — **Katana** (`weapon_katana`, id 14, niveau 257) 7 PT, portée 1, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 77 ; Effect.SHACKLE_TP 0.3–0.4 (1 tours).
- `Weapon.darkKatana` — **Katana sombre** (`weapon_dark_katana`, id 32, niveau 258) 7 PT, portée 1, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 99 ; Effect.VULNERABILITY 15 (1 tours) ; Effect.DAMAGE 44. Passifs : Effect.ALLY_KILLED_TO_AGILITY 100.
- `Weapon.rifle` — **Fusil** (`weapon_rifle`, id 22, niveau 271) 7 PT, portée 7–9, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.DAMAGE 73–79.
- `Weapon.explorerRifle` — **Fusil de l'explorateur** (`weapon_explorer_rifle`, id 24, niveau 272) 7 PT, portée 7–9, zone POINT, lancer CIRCLE, 2 util./tour. Effets : Effect.HEAL 78–86. Passifs : Effect.MOVED_TO_MP 1 (2 tours).
- `Weapon.quantumRifle` — **Fusil quantique** (`weapon_quantum_rifle`, id 40, niveau 281) 10 PT, portée 5–10, zone X_2, lancer CIRCLE, 1 util./tour. Effets : Effect.DAMAGE 68–75 ; Effect.NOVA_DAMAGE 68–75 ; Effect.STEAL_LIFE 0.
- `Weapon.heavySword` — **Épée lourde** (`weapon_heavy_sword`, id 36, niveau 288) 15 PT, portée 1, zone POINT, lancer CIRCLE, 1 util./tour. Effets : Effect.DAMAGE 156–173 ; Effect.ABSOLUTE_VULNERABILITY 60 (1 tours).
- `Weapon.gazor` — **Gazeur** (`weapon_gazor`, id 10, niveau 297) 8 PT, portée 2–7, zone CIRCLE_3, lancer LINE, 2 util./tour. Effets : Effect.POISON 27–32 (3 tours).
- `Weapon.unbridledGazor` — **Gazeur débridé** (`weapon_unbridled_gazor`, id 20, niveau 298) 8 PT, portée 2–7, zone CIRCLE_3, lancer LINE, 2 util./tour. Effets : Effect.DAMAGE 81–85. Passifs : Effect.NOVA_DAMAGE_TO_MAGIC 20.
- `Weapon.mLaser` — **M-Laser** (`weapon_m_laser`, id 12, niveau 299) 8 PT, portée 5–12, zone LASER_LINE, lancer LINE, 2 util./tour. Effets : Effect.DAMAGE 90–100.
- `Weapon.revokedMLaser` — **M-Laser révoqué** (`weapon_revoked_m_laser`, id 21, niveau 300) 8 PT, portée 5–12, zone LASER_LINE, lancer LINE, 2 util./tour. Effets : Effect.POISON 50–60 (2 tours). Passifs : Effect.DAMAGE_TO_STRENGTH 5.

## Puces

- `Chip.apocalypse` — **Apocalypse** (`chip_apocalypse`, id 418, niveau 1) 5 PT, portée 0, zone ENEMIES, lancer CIRCLE, 1 util./tour, sans cooldown. Effets : Effect.KILL 0.
- `Chip.divineProtection` — **Protection divine** (`chip_divine_protection`, id 419, niveau 1) 5 PT, portée 0, zone ALLIES, lancer CIRCLE, 1 util./tour, sans cooldown. Effets : Effect.ADD_STATE 3.
- `Chip.exasperation` — **Exaspération** (`chip_exasperation`, id 425, niveau 1) 0 PT, portée 0, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.TOTAL_DEBUFF 100 ; Effect.VULNERABILITY 20 (1 tours).
- `Chip.piquant` — **Piquant** (`chip_piquant`, id 444, niveau 1) 3 PT, portée 1–3, zone POINT, lancer CIRCLE, sans ligne de vue, utilisations illimitées, sans cooldown. Effets : Effect.DAMAGE 13–17.
- `Chip.capsaicin` — **Capsaïcine** (`chip_capsaicin`, id 445, niveau 1) 6 PT, portée 0, zone CIRCLE_3, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 3. Effets : Effect.DAMAGE 22–28 [ENEMIES|NON_SUMMONS|SUMMONS] ; Effect.POISON 10–14 (2 tours) [ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.sugar` — **Sucre** (`chip_sugar`, id 446, niveau 1) 3 PT, portée 1–3, zone POINT, lancer CIRCLE, sans ligne de vue, utilisations illimitées, sans cooldown. Effets : Effect.HEAL 20–26.
- `Chip.popcorn` — **Pop-corn** (`chip_popcorn`, id 447, niveau 1) 6 PT, portée 0, zone CIRCLE_3, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 3. Effets : Effect.HEAL 35–45 [ALLIES|NON_SUMMONS|SUMMONS].
- `Chip.shock` — **Décharge** (`chip_shock`, id 1, niveau 2) 2 PT, portée 0–6, zone POINT, lancer CIRCLE, 5 util./tour, sans cooldown. Effets : Effect.DAMAGE 7–9.
- `Chip.bandage` — **Bandage** (`chip_bandage`, id 3, niveau 3) 2 PT, portée 0–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.HEAL 23–28.
- `Chip.pebble` — **Caillou** (`chip_pebble`, id 19, niveau 4) 2 PT, portée 0–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.DAMAGE 2–34.
- `Chip.protein` — **Protéines** (`chip_protein`, id 8, niveau 6) 3 PT, portée 0–4, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.RAW_BUFF_STRENGTH 80–100 (2 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.ice` — **Glaçon** (`chip_ice`, id 2, niveau 9) 4 PT, portée 0–8, zone POINT, lancer CIRCLE, 3 util./tour, sans cooldown. Effets : Effect.DAMAGE 17–19.
- `Chip.helmet` — **Casque** (`chip_helmet`, id 21, niveau 10) 3 PT, portée 0–4, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.ABSOLUTE_SHIELD 15 (2 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.rock` — **Rocher** (`chip_rock`, id 7, niveau 13) 5 PT, portée 2–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.DAMAGE 38–39.
- `Chip.motivation` — **Motivation** (`chip_motivation`, id 15, niveau 14) 4 PT, portée 0–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 6. Effets : Effect.RAW_BUFF_TP 2 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.stretching` — **Étirement** (`chip_stretching`, id 9, niveau 17) 3 PT, portée 0–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.RAW_BUFF_AGILITY 80–100 (2 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.wall` — **Mur** (`chip_wall`, id 23, niveau 18) 3 PT, portée 0–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.RELATIVE_SHIELD 4–5 (2 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.spark` — **Étincelle** (`chip_spark`, id 18, niveau 19) 3 PT, portée 0–10, zone POINT, lancer CIRCLE, sans ligne de vue, 5 util./tour, sans cooldown. Effets : Effect.DAMAGE 8–16.
- `Chip.cure` — **Guérison** (`chip_cure`, id 4, niveau 20) 4 PT, portée 0–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.HEAL 38–46.
- `Chip.leatherBoots` — **Bottes de cuir** (`chip_leather_boots`, id 14, niveau 22) 3 PT, portée 0–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.RAW_BUFF_MP 2 (2 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.flash` — **Éclair** (`chip_flash`, id 6, niveau 24) 3 PT, portée 1–10, zone PLUS_1, lancer LINE, utilisations illimitées, cooldown 1. Effets : Effect.DAMAGE 32–35.
- `Chip.flame` — **Flamme** (`chip_flame`, id 5, niveau 29) 4 PT, portée 2–7, zone POINT, lancer CIRCLE, 3 util./tour, sans cooldown. Effets : Effect.DAMAGE 29–31.
- `Chip.knowledge` — **Connaissance** (`chip_knowledge`, id 155, niveau 32) 5 PT, portée 0–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.RAW_BUFF_WISDOM 250–270 (2 tours).
- `Chip.shield` — **Bouclier** (`chip_shield`, id 20, niveau 35) 4 PT, portée 0–4, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.ABSOLUTE_SHIELD 20 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.solidification` — **Solidification** (`chip_solidification`, id 96, niveau 40) 6 PT, portée 0–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.RAW_BUFF_RESISTANCE 180–200 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.venom` — **Venin** (`chip_venom`, id 97, niveau 42) 4 PT, portée 1–10, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.POISON 15–20 (3 tours).
- `Chip.punyBulb` — **Bulbe Chétif** (`chip_puny_bulb`, id 73, niveau 48) 6 PT, portée 1–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 4, cooldown d'équipe. Effets : Effect.SUMMON 1.
- `Chip.stalactite` — **Stalactite** (`chip_stalactite`, id 30, niveau 50) 6 PT, portée 2–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.DAMAGE 64–67.
- `Chip.shuriken` — **Shuriken** (`chip_shuriken`, id 411, niveau 50) 6 PT, portée 1–10, zone POINT, lancer LINE, utilisations illimitées, cooldown 1. Effets : Effect.DAMAGE 50–60 ; Effect.VULNERABILITY 30 (2 tours).
- `Chip.kemuridama` — **Kemuridama** (`chip_kemuridama`, id 412, niveau 50) 8 PT, portée 1–50, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.TELEPORT 0.
- `Chip.alteration` — **Altération** (`chip_alteration`, id 141, niveau 53) 3 PT, portée 6–12, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.NOVA_DAMAGE 18–20.
- `Chip.drip` — **Perfusion** (`chip_drip`, id 10, niveau 56) 5 PT, portée 2–6, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.HEAL 40–45.
- `Chip.liberation` — **Libération** (`chip_liberation`, id 34, niveau 60) 5 PT, portée 0–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.DEBUFF 40.
- `Chip.corn` — **Maïs** (`chip_corn`, id 164, niveau 63) 8 PT, portée 1–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 8. Effets : Effect.SUMMON 9.
- `Chip.tranquilizer` — **Tranquillisant** (`chip_tranquilizer`, id 94, niveau 65) 3 PT, portée 1–8, zone PLUS_1, lancer CIRCLE, 4 util./tour, sans cooldown. Effets : Effect.SHACKLE_TP 0.5–0.6 (1 tours).
- `Chip.armoring` — **Blindage** (`chip_armoring`, id 67, niveau 68) 5 PT, portée 0–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.BOOST_MAX_LIFE 25–30.
- `Chip.jump` — **Saut** (`chip_jump`, id 144, niveau 70) 4 PT, portée 1–3, zone POINT, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 3. Effets : Effect.TELEPORT 0 ; Effect.RAW_BUFF_AGILITY 100 (2 tours).
- `Chip.armor` — **Armure** (`chip_armor`, id 22, niveau 74) 6 PT, portée 0–4, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.ABSOLUTE_SHIELD 25 (4 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.rockfall` — **Éboulement** (`chip_rockfall`, id 32, niveau 77) 5 PT, portée 5–7, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.DAMAGE 50–58.
- `Chip.vaccine` — **Vaccin** (`chip_vaccine`, id 11, niveau 80) 6 PT, portée 0–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.HEAL 38–42 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.mutation` — **Mutation** (`chip_mutation`, id 159, niveau 83) 7 PT, portée 0–8, zone SQUARE_2, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.NOVA_VITALITY 15–20.
- `Chip.prism` — **Prisme** (`chip_prism`, id 276, niveau 92) 6 PT, portée 0–6, zone POINT, lancer STAR_INVERTED, utilisations illimitées, cooldown 6. Effets : Effect.RAW_BUFF_STRENGTH 60 (2 tours) ; Effect.RAW_BUFF_WISDOM 60 (2 tours) ; Effect.RAW_BUFF_AGILITY 60 (2 tours) ; Effect.RAW_BUFF_RESISTANCE 60 (2 tours) ; Effect.RAW_BUFF_SCIENCE 60 (2 tours) ; Effect.RAW_BUFF_MAGIC 60 (2 tours).
- `Chip.slowDown` — **Ralentissement** (`chip_slow_down`, id 92, niveau 98) 3 PT, portée 1–8, zone POINT, lancer CIRCLE, 4 util./tour, sans cooldown. Effets : Effect.SHACKLE_MP 0.3–0.4 (1 tours).
- `Chip.iceberg` — **Iceberg** (`chip_iceberg`, id 31, niveau 100) 7 PT, portée 3–5, zone CIRCLE_2, lancer LINE, utilisations illimitées, cooldown 3. Effets : Effect.DAMAGE 82–90.
- `Chip.fireBall` — **Boule de feu** (`chip_fire_ball`, id 413, niveau 100) 6 PT, portée 2–6, zone PLUS_1, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.DAMAGE 80–90.
- `Chip.trebuchet` — **Trébuchet** (`chip_trebuchet`, id 414, niveau 100) 12 PT, portée 3–50, zone CIRCLE_3, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 5. Effets : Effect.DAMAGE 200–220.
- `Chip.kill` — **Tuer** (`chip_kill`, id 417, niveau 100) 1 PT, portée 0–50, zone POINT, lancer CIRCLE, 1 util./tour, sans cooldown. Effets : Effect.KILL 0.
- `Chip.rockyBulb` — **Bulbe Rocheux** (`chip_rocky_bulb`, id 76, niveau 105) 10 PT, portée 1–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5, cooldown d'équipe. Effets : Effect.SUMMON 4.
- `Chip.ferocity` — **Férocité** (`chip_ferocity`, id 102, niveau 107) 5 PT, portée 1–8, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.BUFF_STRENGTH 50–60 (2 tours) [ALLIES|CASTER|SUMMONS].
- `Chip.loam` — **Terreau** (`chip_loam`, id 89, niveau 111) 4 PT, portée 1–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.BOOST_MAX_LIFE 43–48 [ALLIES|CASTER|SUMMONS] ; Effect.BOOST_MAX_LIFE 13–18 [ALLIES|NON_SUMMONS].
- `Chip.antidote` — **Antidote** (`chip_antidote`, id 110, niveau 114) 3 PT, portée 0–4, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.ANTIDOTE 100 [ALLIES|CASTER|NON_SUMMONS|SUMMONS] ; Effect.HEAL 25–35 [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.rampart` — **Rempart** (`chip_rampart`, id 24, niveau 117) 5 PT, portée 2–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.RELATIVE_SHIELD 9–10 (3 tours) [ALLIES|CASTER|SUMMONS] ; Effect.RELATIVE_SHIELD 4–5 (3 tours) [ALLIES|CASTER|NON_SUMMONS].
- `Chip.whip` — **Fouet** (`chip_whip`, id 88, niveau 119) 4 PT, portée 0–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.BUFF_TP 0.6–0.7 (2 tours) [ALLIES|CASTER|SUMMONS].
- `Chip.grapple` — **Grappin** (`chip_grapple`, id 162, niveau 120) 3 PT, portée 1–8, zone FIRST_INLINE, lancer LINE, 4 util./tour, sans cooldown. Effets : Effect.ATTRACT 0 ; Effect.RAW_BUFF_WISDOM 30–40 (1 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS] ; Effect.SHACKLE_AGILITY 15–20 (1 tours) [CASTER|ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.regeneration` — **Régénération** (`chip_regeneration`, id 35, niveau 122) 8 PT, portée 0–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown infini. Effets : Effect.HEAL 500.
- `Chip.toxin` — **Toxine** (`chip_toxin`, id 98, niveau 125) 5 PT, portée 1–7, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.POISON 25–35 (3 tours).
- `Chip.warmUp` — **Échauffement** (`chip_warm_up`, id 28, niveau 127) 7 PT, portée 0–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.RAW_BUFF_AGILITY 170–190 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.icedBulb` — **Bulbe Glacé** (`chip_iced_bulb`, id 77, niveau 130) 12 PT, portée 1–2, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5, cooldown d'équipe. Effets : Effect.SUMMON 5.
- `Chip.thorn` — **Épine** (`chip_thorn`, id 100, niveau 132) 4 PT, portée 0–3, zone PLUS_1, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.DAMAGE_RETURN 3–4 (2 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.steroid` — **Stéroïdes** (`chip_steroid`, id 25, niveau 134) 7 PT, portée 0–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.RAW_BUFF_STRENGTH 150–170 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.covetousness` — **Convoitise** (`chip_covetousness`, id 120, niveau 139) 2 PT, portée 0–8, zone X_2, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.RAW_BUFF_TP 1 (2 tours) [CASTER|ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.boxingGlove` — **Gant de boxe** (`chip_boxing_glove`, id 163, niveau 140) 3 PT, portée 2–8, zone FIRST_INLINE, lancer LINE, 4 util./tour, sans cooldown. Effets : Effect.PUSH 0 ; Effect.RAW_BUFF_RESISTANCE 30–40 (1 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS] ; Effect.SHACKLE_STRENGTH 10–15 (1 tours) [CASTER|ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.carapace` — **Carapace** (`chip_carapace`, id 81, niveau 141) 5 PT, portée 1–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.ABSOLUTE_SHIELD 55 (3 tours) [ALLIES|CASTER|SUMMONS] ; Effect.ABSOLUTE_SHIELD 15–20 (3 tours) [ALLIES|CASTER|NON_SUMMONS].
- `Chip.acceleration` — **Accélération** (`chip_acceleration`, id 91, niveau 143) 4 PT, portée 0–8, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.BUFF_MP 0.4–0.5 (2 tours) [ALLIES|CASTER|SUMMONS].
- `Chip.soporific` — **Somnifère** (`chip_soporific`, id 95, niveau 145) 5 PT, portée 1–6, zone CIRCLE_3, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.SHACKLE_TP 0.4–0.5 (3 tours).
- `Chip.punishment` — **Châtiment** (`chip_punishment`, id 114, niveau 147) 5 PT, portée 1, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.LIFE_DAMAGE 25 ; Effect.LIFE_DAMAGE 75.
- `Chip.manumission` — **Affranchissement** (`chip_manumission`, id 174, niveau 149) 6 PT, portée 0–5, zone POINT, lancer LINE, utilisations illimitées, cooldown 5. Effets : Effect.REMOVE_SHACKLES 0 ; Effect.RAW_BUFF_TP 2 (1 tours).
- `Chip.inversion` — **Inversion** (`chip_inversion`, id 68, niveau 150) 4 PT, portée 1–14, zone POINT, lancer LINE, utilisations illimitées, cooldown 4. Effets : Effect.INVERT 0 ; Effect.HEAL 50 [ALLIES|CASTER|NON_SUMMONS|SUMMONS] ; Effect.VULNERABILITY 20 (1 tours) [CASTER|ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.prototaxite` — **Prototaxite** (`chip_prototaxite`, id 441, niveau 152) 6 PT, portée 1–10, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.SUMMON 13.
- `Chip.adrenaline` — **Adrénaline** (`chip_adrenaline`, id 16, niveau 156) 1 PT, portée 0–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 7. Effets : Effect.RAW_BUFF_TP 5 (1 tours) [ALLIES|CASTER|NON_SUMMONS].
- `Chip.crushing` — **Écrasement** (`chip_crushing`, id 169, niveau 158) 6 PT, portée 1–8, zone POINT, lancer STAR, utilisations illimitées, cooldown 1. Effets : Effect.SHACKLE_AGILITY 45–49 (2 tours).
- `Chip.meteorite` — **Météorite** (`chip_meteorite`, id 36, niveau 160) 8 PT, portée 5–9, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.DAMAGE 70–80.
- `Chip.repotting` — **Rempotage** (`chip_repotting`, id 157, niveau 163) 4 PT, portée 1–14, zone POINT, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 2. Effets : Effect.INVERT 0 [ALLIES|CASTER|SUMMONS] ; Effect.DAMAGE 18–20 [ALLIES|CASTER|SUMMONS].
- `Chip.wizardry` — **Sorcellerie** (`chip_wizardry`, id 156, niveau 166) 6 PT, portée 0–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.RAW_BUFF_MAGIC 150–170 (2 tours).
- `Chip.remission` — **Rémission** (`chip_remission`, id 80, niveau 170) 5 PT, portée 0–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.HEAL 66–77 [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.devilStrike` — **Frappe du démon** (`chip_devil_strike`, id 85, niveau 171) 6 PT, portée 0, zone CIRCLE_3, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.DAMAGE 25 ; Effect.DAMAGE 25 ; Effect.DAMAGE 25 ; Effect.DAMAGE 25 ; Effect.DAMAGE 25.
- `Chip.healerBulb` — **Bulbe Guérisseur** (`chip_healer_bulb`, id 75, niveau 174) 14 PT, portée 1–2, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 7, cooldown d'équipe. Effets : Effect.SUMMON 3.
- `Chip.wingedBoots` — **Bottes ailées** (`chip_winged_boots`, id 13, niveau 175) 6 PT, portée 0–2, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.RAW_BUFF_MP 3 (1 tours) [ALLIES|CASTER|NON_SUMMONS].
- `Chip.vampirization` — **Vampirisation** (`chip_vampirization`, id 121, niveau 177) 6 PT, portée 0–8, zone PLUS_3, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.HEAL 42–44 [CASTER|ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.chilliPepper` — **Piment** (`chip_chilli_pepper`, id 165, niveau 179) 10 PT, portée 1–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 8. Effets : Effect.SUMMON 10.
- `Chip.lightning` — **Foudre** (`chip_lightning`, id 33, niveau 180) 4 PT, portée 2–5, zone CIRCLE_2, lancer LINE, 3 util./tour, sans cooldown. Effets : Effect.DAMAGE 35–47 [ALLIES|ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.collar` — **Collier** (`chip_collar`, id 103, niveau 182) 5 PT, portée 1–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.BUFF_WISDOM 80–90 (2 tours) [ALLIES|CASTER|SUMMONS].
- `Chip.ballAndChain` — **Boulet** (`chip_ball_and_chain`, id 93, niveau 184) 5 PT, portée 1–6, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.SHACKLE_MP 0.4–0.5 (2 tours).
- `Chip.fireBulb` — **Bulbe Enflammé** (`chip_fire_bulb`, id 74, niveau 190) 14 PT, portée 2–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 6, cooldown d'équipe. Effets : Effect.SUMMON 2.
- `Chip.precipitation` — **Précipitation** (`chip_precipitation`, id 122, niveau 192) 3 PT, portée 0–8, zone X_2, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.RAW_BUFF_MP 1 (2 tours) [CASTER|ENEMIES|NON_SUMMONS|SUMMONS].
- `Chip.fortress` — **Forteresse** (`chip_fortress`, id 29, niveau 194) 6 PT, portée 0–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.RELATIVE_SHIELD 7–8 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.hemorrhage` — **Hémorragie** (`chip_hemorrhage`, id 273, niveau 196) 10 PT, portée 1–2, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.ADD_STATE 2 (1 tours).
- `Chip.reflexes` — **Réflexes** (`chip_reflexes`, id 27, niveau 197) 5 PT, portée 0–6, zone PLUS_3, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.BUFF_AGILITY 35–40 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.serum` — **Sérum** (`chip_serum`, id 168, niveau 199) 8 PT, portée 0–6, zone SQUARE_1, lancer LINE, utilisations illimitées, cooldown 5. Effets : Effect.HEAL 50–55 (4 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.teleportation` — **Téléportation** (`chip_teleportation`, id 59, niveau 200) 9 PT, portée 1–12, zone POINT, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 10. Effets : Effect.TELEPORT 0 ; Effect.BOOST_MAX_LIFE 15–20.
- `Chip.awakening` — **Réveil** (`chip_awakening`, id 415, niveau 200) 0 PT, portée 1–50, zone POINT, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 1. Effets : Effect.RESURRECT 0 ; Effect.ADD_STATE 3.
- `Chip.thunder` — **Tonnerre** (`chip_thunder`, id 416, niveau 200) 8 PT, portée 3–8, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.DAMAGE 100–120.
- `Chip.sevenLeagueBoots` — **Bottes de 7 lieues** (`chip_seven_league_boots`, id 12, niveau 203) 4 PT, portée 0–8, zone PLUS_2, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.BUFF_MP 0.4–0.5 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.fertilizer` — **Fertilisant** (`chip_fertilizer`, id 90, niveau 205) 6 PT, portée 1–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.BOOST_MAX_LIFE 80–90 [ALLIES|CASTER|SUMMONS].
- `Chip.doping` — **Dopage** (`chip_doping`, id 26, niveau 207) 5 PT, portée 0–6, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.BUFF_STRENGTH 30–35 (3 tours) [ALLIES|NON_SUMMONS|SUMMONS] ; Effect.AFTEREFFECT 30–35 (3 tours) [ALLIES|NON_SUMMONS|SUMMONS].
- `Chip.burning` — **Brûlis** (`chip_burning`, id 105, niveau 209) 5 PT, portée 4–6, zone CIRCLE_3, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.DAMAGE 78–87 [ENEMIES|SUMMONS] ; Effect.POISON 78–87 (1 tours) [ENEMIES|SUMMONS] ; Effect.KILL 0 [ALLIES|CASTER|SUMMONS].
- `Chip.plague` — **Peste** (`chip_plague`, id 99, niveau 210) 6 PT, portée 1–5, zone CIRCLE_3, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.POISON 40–50 (4 tours).
- `Chip.wizardBulb` — **Bulbe magicien** (`chip_wizard_bulb`, id 142, niveau 215) 15 PT, portée 1–3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 7, cooldown d'équipe. Effets : Effect.SUMMON 8.
- `Chip.covid` — **La Covid-19** (`chip_covid`, id 152, niveau 220) 8 PT, portée 0–2, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 7. Effets : Effect.PROPAGATION 2 ; Effect.POISON 69–79 (7 tours).
- `Chip.desintegration` — **Désintégration** (`chip_desintegration`, id 160, niveau 223) 8 PT, portée 1–6, zone SQUARE_1, lancer LINE, utilisations illimitées, cooldown 2. Effets : Effect.NOVA_DAMAGE 70–80.
- `Chip.rage` — **Rage** (`chip_rage`, id 17, niveau 226) 4 PT, portée 0–8, zone CIRCLE_3, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.BUFF_TP 0.5–0.6 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.elevation` — **Élévation** (`chip_elevation`, id 154, niveau 228) 6 PT, portée 0–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown infini. Effets : Effect.BOOST_MAX_LIFE 80.
- `Chip.metallicBulb` — **Bulbe Métallique** (`chip_metallic_bulb`, id 79, niveau 230) 16 PT, portée 1, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 7, cooldown d'équipe. Effets : Effect.SUMMON 7.
- `Chip.superinfection` — **Surinfection** (`chip_superinfection`, id 443, niveau 232) 7 PT, portée 1–2, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.SUPERINFECTION 50.
- `Chip.bark` — **Écorce** (`chip_bark`, id 104, niveau 234) 5 PT, portée 1–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.BUFF_RESISTANCE 60–70 (2 tours) [ALLIES|CASTER|SUMMONS].
- `Chip.fracture` — **Fracture** (`chip_fracture`, id 106, niveau 240) 4 PT, portée 1–6, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 1. Effets : Effect.SHACKLE_STRENGTH 17–22 (2 tours).
- `Chip.dome` — **Dôme** (`chip_dome`, id 173, niveau 243) 9 PT, portée 0, zone CIRCLE_3, lancer CIRCLE, utilisations illimitées, cooldown 8. Effets : Effect.RELATIVE_SHIELD 11–13 (3 tours) [ALLIES|NON_SUMMONS|SUMMONS].
- `Chip.mirror` — **Miroir** (`chip_mirror`, id 101, niveau 246) 5 PT, portée 0–2, zone CIRCLE_2, lancer CIRCLE, utilisations illimitées, cooldown 4. Effets : Effect.DAMAGE_RETURN 5–6 (3 tours) [ALLIES|CASTER|NON_SUMMONS|SUMMONS].
- `Chip.savantBulb` — **Bulbe Savant** (`chip_savant_bulb`, id 167, niveau 250) 16 PT, portée 1–4, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 7, cooldown d'équipe. Effets : Effect.SUMMON 12.
- `Chip.transmutation` — **Transmutation** (`chip_transmutation`, id 161, niveau 252) 8 PT, portée 1–6, zone SQUARE_1, lancer LINE, utilisations illimitées, cooldown 9. Effets : Effect.NOVA_VITALITY 40–44.
- `Chip.therapy` — **Thérapie** (`chip_therapy`, id 158, niveau 260) 7 PT, portée 1–5, zone PLUS_2, lancer CIRCLE, utilisations illimitées, cooldown 2. Effets : Effect.HEAL 75–80.
- `Chip.brainwashing` — **Décervelage** (`chip_brainwashing`, id 170, niveau 266) 6 PT, portée 1–8, zone POINT, lancer STAR, utilisations illimitées, cooldown 1. Effets : Effect.SHACKLE_WISDOM 32–39 (2 tours).
- `Chip.maturation` — **Maturation** (`chip_maturation`, id 442, niveau 267) 12 PT, portée 1–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 5. Effets : Effect.BOOST_MAX_LIFE 75 [ALLIES|CASTER|SUMMONS] ; Effect.RAW_BUFF_POWER 5 [ALLIES|CASTER|SUMMONS].
- `Chip.tacticianBulb` — **Bulbe Tacticien** (`chip_tactician_bulb`, id 166, niveau 270) 16 PT, portée 3, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 7, cooldown d'équipe. Effets : Effect.SUMMON 11.
- `Chip.bramble` — **Ronce** (`chip_bramble`, id 172, niveau 278) 4 PT, portée 0–7, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 8. Effets : Effect.DAMAGE_RETURN 25 (1 tours).
- `Chip.lightningBulb` — **Bulbe Foudroyant** (`chip_lightning_bulb`, id 78, niveau 280) 16 PT, portée 1–5, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 6, cooldown d'équipe. Effets : Effect.SUMMON 6.
- `Chip.arsenic` — **Arsenic** (`chip_arsenic`, id 171, niveau 285) 8 PT, portée 3–4, zone POINT, lancer CIRCLE, sans ligne de vue, utilisations illimitées, cooldown 2. Effets : Effect.POISON 62–67 (2 tours).
- `Chip.plasma` — **Plasma** (`chip_plasma`, id 143, niveau 290) 9 PT, portée 0–6, zone PLUS_2, lancer CIRCLE, utilisations illimitées, cooldown 3. Effets : Effect.DAMAGE 37–39.
- `Chip.resurrection` — **Résurrection** (`chip_resurrection`, id 84, niveau 301) 18 PT, portée 1–2, zone POINT, lancer CIRCLE, utilisations illimitées, cooldown 15. Effets : Effect.RESURRECT 0.
