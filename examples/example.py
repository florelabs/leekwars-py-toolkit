# IA d'exemple : couvre les idiomes de l'API objet Python Leek Wars et sert de test du stub
# (__builtins__.pyi) : `npx pyright` doit passer sans erreur.
#
# Modèle d'exécution (cf docs/runtime.md) : ce fichier est évalué UNE fois au tour 1 (les globales
# persistent tout le combat), puis turn() est rejouée à chaque tour.

from helpers import best_damage_chip, kite_cell

history: list[int] = []  # persiste entre les tours


def beforeFight() -> None:
    """Hook optionnel, appelé avant le tour 1 (ex. choisir un loadout). Ne pas agir ici."""
    pass


def pick_target() -> Entity | None:
    # getNearestEnemy() peut renvoyer None (dernier ennemi mort en solo, etc.) même si le stub dit Entity.
    enemies = [e for e in Fight.getAliveEnemies() if not e.summoned]
    if not enemies:
        return Fight.getNearestEnemy()
    return min(enemies, key=lambda e: (e.life, Fight.me.distance(e)))


def turn() -> None:
    me = Fight.me
    enemy = pick_target()
    if enemy is None:
        return
    history.append(enemy.id)

    # Équipement : les armes sont des instances comparables par identité.
    if me.weapon is not Weapon.pistol and Weapon.pistol in me.weapons:
        me.setWeapon(Weapon.pistol)  # coûte 1 PT

    # Soin si nécessaire (les puces aussi sont des singletons ; cooldown lisible).
    if me.life < me.maxLife // 2 and Chip.bandage in me.chips and Chip.bandage.currentCooldown == 0:
        me.useChip(Chip.bandage, me)

    # Se placer : d'où puis-je tirer sur lui ?
    cell = me.weaponCell(enemy)
    if cell is not None and cell is not me.cell:
        me.moveToward(cell)

    # Tirer tant que possible : Fight.Use.SUCCESS = 1, Fight.Use.CRITICAL = 2, échec <= 0.
    while me.tp >= Weapon.pistol.cost and me.canUseWeapon(enemy):
        if me.useWeapon(enemy) <= 0:
            break

    # Puce de dégâts la plus rentable avec les PT restants.
    chip = best_damage_chip(me, enemy)
    if chip is not None and me.canUseChip(chip, enemy):
        me.useChip(chip, enemy)

    # Se replier avec les PM restants.
    if me.mp > 0:
        target = kite_cell(me, enemy)
        if target is not None:
            me.moveToward(target)
            Debug.mark(target, Color.GREEN)

    # Lecture des effets actifs : objets typés, pas des tableaux.
    for effect in me.effects:
        if effect.type == Effect.POISON:
            print(f"empoisonné {effect.value} pendant {effect.turns} tours par {effect.caster.name}")

    # Sous-types d'entités.
    for e in Fight.getEnemies():
        if isinstance(e, Bulb) and e.type == Bulb.Type.HEALER:
            Debug.markText(e.cell, "heal", Color.RED)

    # Budget : System.operations vs System.maxOperations pour borner une recherche.
    if System.operations > System.maxOperations * 0.8:
        Debug.log("budget presque épuisé", Color.RED)

    # Registres persistants entre combats (clé/valeur str).
    Registers.set("last_target", str(enemy.id))
