# Python
> Programmation

<center><img height=90 src="/image/language/python.svg"></center>
<br>

Depuis la version 2.49, en plus du [[LeekScript]], vous pouvez écrire les [[intelligence artificielle|intelligences artificielles]] de vos poireaux en **Python** (ou en [[JavaScript et TypeScript|JavaScript / TypeScript]]). Les IA s'exécutent dans un environnement sécurisé et déterministe, avec accès à toute l'API de combat du jeu, et peuvent affronter des IA écrites dans n'importe quel autre langage.

- **Python 3.12** (moteur GraalPy)

<div class="tip">
<div class="leeky"></div>
<p>Débutant ? Suivez le <a href="/help/tutorial/python">tutoriel Python</a> pour apprendre à coder votre première IA, pas à pas.</p>
</div>

## Choisir le langage

Le langage d'une IA est déterminé par l'**extension** de son fichier :

| Langage | Extension |
|---------|-----------|
| [[LeekScript]] | *(aucune)* |
| <a href="/encyclopedia/fr/JavaScript_et_TypeScript">JavaScript</a> | `.js` ou `.mjs` |
| <a href="/encyclopedia/fr/JavaScript_et_TypeScript">TypeScript</a> | `.ts` ou `.mts` |
| **Python** | `.py` |

Le langage se choisit à la création d'un fichier (bouton « Nouvelle IA » de l'éditeur) ou comme langage par défaut de la première IA à l'inscription. Renommer un fichier en changeant son extension change son langage.

## Point d'entrée : turn()

À chaque tour, le moteur exécute votre IA. Deux façons d'écrire :

**IA simple** : écrivez directement votre code, il est rejoué à chaque tour :

```python
me = Fight.me
me.setWeapon(Weapon.pistol)
enemy = Fight.getNearestEnemy()
me.moveToward(enemy)
me.useWeapon(enemy)
```

**IA avec état** : définissez une fonction `turn()`. Le corps du fichier n'est évalué qu'une seule fois (déclarez-y vos classes et variables persistantes), puis `turn()` est rejouée à chaque tour :

```python
memoire = []           # persiste entre les tours

def turn():
    me = Fight.me
    enemy = Fight.getNearestEnemy()
    me.moveToward(enemy)
    me.useWeapon(enemy)
```

## L'API de combat

L'API du jeu est exposée sous forme **orientée objet**, et garde ses noms camelCase en Python : `me.setWeapon(...)`, `Fight.getNearestEnemy()`. Il n'y a pas de variable globale `me` : votre entité s'obtient via `Fight.me`.

Contrairement au LeekScript, il n'y a ni fonctions globales ni constantes « plates » (`getNearestEnemy()`, `WEAPON_PISTOL`…) : toute l'API passe par les objets ci-dessous.

### Arborescence des classes

```
Entity                    une entité du combat (stats, position, effets…)
├── Leek                  un poireau
├── Turret                une tourelle (combat en équipe)
├── Bulb                  une invocation           (sous-type : Bulb.Type)
├── Chest                 un coffre                (sous-type : Chest.Type)
├── Mob                   un monstre ou un boss    (sous-type : Mob.Type)
└── Me                    VOTRE entité, qui porte les actions (via Fight.me)

Cell                      une case du terrain
Item                      base commune arme / puce
├── Weapon                une arme  (instances : Weapon.pistol, …)
└── Chip                  une puce  (instances : Chip.bandage, …)
Effect                    un effet actif sur une entité
Feature                   une caractéristique portée par une arme ou une puce
```

Les entités renvoyées par l'API sont typées : `isinstance(enemy, Leek)`, `isinstance(enemy, Bulb)`…

| Classe | Membres principaux |
|--------|--------------------|
| `Entity` | `life`, `maxLife`, `tp`, `mp`, `strength`, `agility`, `wisdom`, `resistance`, `science`, `magic`, `level`, `name`, `cell`, `weapon`, `weapons`, `chips`, `effects`, `states`, `summons`, `alive`, `dead`, `isAlly()`, `isEnemy()`, `distance(cible)` |
| `Me` | tout `Entity`, plus les actions : `moveToward(cible)`, `moveAwayFrom(cible)`, `useWeapon(cible)`, `useChip(puce, cible)`, `setWeapon(arme)`, `say(message)`, `summon(puce, case, ia)`, `canUseWeapon(cible)`, `weaponCell(cible)`, `chipCells(puce, cible)`, `weaponTargets(case)`… |
| `Cell` | `x`, `y`, `empty`, `obstacle`, `entity`, `distance(cible)`, `pathLength(cible)`, `lineOfSight(cible)`, `path(cible)` |
| `Weapon` / `Chip` | `cost`, `minRange`, `maxRange`, `area`, `launchType`, `maxUses`, `needsLos`, `features` (plus `cooldown` et `currentCooldown` pour `Chip`) |
| `Effect` | `type`, `value`, `caster`, `turns`, `critical`, `item`, `target` |
| `Feature` | `type`, `minValue`, `maxValue`, `turns`, `targets` |

À côté des classes, quatre **singletons** :

| Singleton | Rôle | Membres principaux |
|-----------|------|--------------------|
| `Fight` | le combat | `me`, `turn`, `getNearestEnemy()`, `getFarthestEnemy()`, `getEnemies()`, `getAliveEnemies()`, `getAllies()`, `getAlliedTurret()`… |
| `Field` | le terrain | `cellFromXY(x, y)`, `getObstacles()`, `distance(a, b)`, `pathLength(a, b)`, `lineOfSight(a, b)`, `path(a, b)` |
| `Registers` | stockage persistant entre les combats | `get(clé)`, `set(clé, valeur)`, `delete(clé)`, `all()` |
| `Debug` | visualisation sur le terrain | `mark(cases, couleur)`, `markText(cases, texte)`, `show(case)`, `clearMarks()`, `pause()` |

### Les constantes

Les constantes sont rangées par famille, sous deux formes :

- **Instances** (armes et puces) : en camelCase, comparables par référence : `Weapon.pistol`, `Chip.bandage`, `me.weapon is Weapon.pistol`.
- **Catégories** : en MAJUSCULES : `Effect.DAMAGE`, `State.UNHEALABLE`, `Entity.Stat.STRENGTH`, `Entity.Type.LEEK`, `Cell.Type.EMPTY`, `Item.Area.CIRCLE_1`, `Item.LaunchType.LINE`, `Fight.Type.SOLO`, `Fight.Context.GARDEN`, `Field.NEXUS`…

L'autocomplétion de l'éditeur (`Weapon.`, `Effect.`, `Entity.Stat.`…) liste tous les membres disponibles, avec la vérification de types en direct (Pyright).

## Plusieurs fichiers

Découpez votre IA en modules avec l'`import` Python classique :

```python
# utils.py
def best_target():
    ...
```

```python
# main.py
from utils import best_target
```

Seuls vos propres fichiers sont accessibles. Les noms de modules suivent les règles Python : pas de tirets, utilisez des underscores. Les imports circulaires ne sont pas autorisés.

## La bibliothèque standard

La bibliothèque standard de Python 3.12 est disponible : `math`, `itertools`, `collections`, `heapq`, `functools`, `random`… En revanche, pas de paquets externes (pip), et les modules d'accès au système (fichiers, réseau, processus) sont inaccessibles.

## Environnement d'exécution

- **Combats reproductibles** : le module `random` est initialisé par la graine du combat et l'horloge (`time`, `datetime`) est figée, pour que les combats soient rejouables à l'identique.
- **`print()`** est redirigé vers le journal de combat, comme `debug()` en LeekScript : sa sortie apparaît dans le rapport.
- **Budget d'exécution** : comme en LeekScript, chaque tour dispose d'un budget d'opérations et de mémoire selon le niveau du poireau, calibré pour être comparable entre les langages. Dépasser le budget interrompt le tour.

## Voir aussi

- [[LeekScript]] : le langage historique de Leek Wars
- [[JavaScript et TypeScript]] : écrire son IA en JavaScript ou TypeScript
- <a href="/help/tutorial/python">Tutoriel Python</a> : apprendre à coder son IA pas à pas
- <a href="/help/documentation">Documentation</a> des fonctions et constantes

