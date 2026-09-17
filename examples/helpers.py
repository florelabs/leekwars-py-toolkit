# Module importé par example.py : l'API objet (Fight, Cell, Weapon...) est posée sur `builtins` côté
# serveur, donc visible depuis les modules importés aussi, sans import. Noms de modules : underscores
# uniquement (pas de tirets), pas d'imports circulaires.


def kite_cell(me: Me, enemy: Entity, max_candidates: int = 60) -> Cell | None:
    """Case atteignable avec les PM restants qui maximise la distance à l'ennemi hors de sa ligne de vue."""
    best: Cell | None = None
    best_score = -1
    origin = me.cell
    for dx in range(-me.mp, me.mp + 1):
        for dy in range(-me.mp, me.mp + 1):
            if abs(dx) + abs(dy) > me.mp:
                continue
            c = Field.cellFromXY(origin.x + dx, origin.y + dy)
            if c is None or not c.empty:
                continue
            if c.pathLength(origin) > me.mp:
                continue
            score = c.distance(enemy) * 2 + (0 if c.lineOfSight(enemy) else 5)
            if score > best_score:
                best, best_score = c, score
            max_candidates -= 1
            if max_candidates == 0:
                return best
    return best


def best_damage_chip(me: Me, enemy: Entity) -> Chip | None:
    """Puce de dégâts utilisable (PT, cooldown, portée) au meilleur ratio dégâts moyens / PT."""
    best: Chip | None = None
    best_ratio = 0.0
    for chip in me.chips:
        if chip.cost > me.tp or chip.currentCooldown > 0:
            continue
        dmg = 0.0
        for f in chip.features:
            if f.type == Effect.DAMAGE:
                dmg += (f.minValue + f.maxValue) / 2
        if dmg == 0:
            continue
        ratio = dmg / chip.cost
        if ratio > best_ratio and me.canUseChip(chip, enemy):
            best, best_ratio = chip, ratio
    return best
