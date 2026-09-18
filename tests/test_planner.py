from danger import Danger
from planner import Planner
from scenario import PISTOL, cell, leek, open_grid, world
from skills import BUFF_MP, DAMAGE, HEAL, SHACKLE_MP, TELEPORT, make
from tuning import Profile

TELEPORT_CHIP = make("c:teleportation", TELEPORT, cost=9, min_range=1, max_range=12, min_v=0, max_v=0, los=False)
BANDAGE = make("c:bandage", HEAL, cost=2, min_range=0, max_range=6, min_v=23, max_v=28)
BOOTS = make("c:boots", BUFF_MP, cost=3, min_range=0, max_range=5, min_v=3, max_v=3)
CHAIN = make("c:chain", SHACKLE_MP, cost=5, min_range=1, max_range=6, min_v=3, max_v=3)


def kinds(plan):
    return [(a.kind, a.skill.key if a.skill else None, a.n) for a in plan.actions]


def test_walk_in_range_and_shoot_four_times():
    g = open_grid(16, 5)
    me = leek(1, cell(g, 0, 2))
    enemy = leek(2, cell(g, 12, 2), tp=10, mp=3, enemy=True)
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    shots = [a for a in plan.actions if a.kind == "weapon"]
    assert sum(a.n for a in shots) == 4
    moves = [a.cell for a in plan.actions if a.kind == "move" and a.cell is not None]
    assert moves and g.dist(moves[0], enemy.cell) <= 7
    assert plan.value > 0


def test_retreat_out_of_reach_when_possible():
    g = open_grid(20, 3)
    me = leek(1, cell(g, 9, 1), mp=6)
    # Ennemi lent à courte portée : après avoir tiré, on peut sortir de sa zone (2 PM + 3 de portée = 5).
    knife = make("w:knife", DAMAGE, cost=4, min_range=1, max_range=3, min_v=30, max_v=40, max_uses=2, is_weapon=True)
    enemy = leek(2, cell(g, 12, 1), tp=10, mp=2, enemy=True, skills=[knife])
    plan = Planner(world(g, me, [enemy]), Profile(max_stops=1)).plan()
    assert plan.danger == 0.0
    assert g.dist(plan.end_cell, enemy.cell) > 5
    assert any(a.kind == "weapon" for a in plan.actions)


def test_teleport_when_walking_cannot_reach():
    g = open_grid(24, 3)
    me = leek(1, cell(g, 0, 1), mp=2, skills=[PISTOL, TELEPORT_CHIP])
    # Ennemi faible : le saut (9 PT + malus w_tp_reserve) doit rapporter plus que le danger encaissé.
    enemy = leek(2, cell(g, 16, 1), tp=6, mp=3, strength=0, enemy=True)
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert any(a.kind == "teleport" for a in plan.actions)
    assert any(a.kind == "weapon" for a in plan.actions)
    # 9 PT de téléport + 3 tirs à 3 PT + 1 changement d'arme max = 20
    assert sum(a.n for a in plan.actions if a.kind == "weapon") == 3


def test_heal_when_nothing_else_to_do():
    g = open_grid(30, 3)
    me = leek(1, cell(g, 0, 1), life=200, max_life=1000, skills=[PISTOL, BANDAGE])
    enemy = leek(2, cell(g, 29, 1), tp=10, mp=3, enemy=True)
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert ("chip", "c:bandage", 1) in kinds(plan)


def test_mp_buff_context_used_to_reach():
    g = open_grid(24, 3)
    me = leek(1, cell(g, 0, 1), mp=3, skills=[PISTOL, BOOTS])
    enemy = leek(2, cell(g, 13, 1), tp=10, mp=3, enemy=True)  # distance 13 : 7 de portée + 6 de marche > 3 PM
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert kinds(plan)[0] == ("chip", "c:boots", 1)
    assert any(a.kind == "weapon" for a in plan.actions)


def test_shackle_variant_makes_end_cell_safe():
    g = open_grid(24, 3)
    me = leek(1, cell(g, 8, 1), mp=4, skills=[PISTOL, CHAIN])
    enemy = leek(2, cell(g, 14, 1), tp=10, mp=3, enemy=True)
    plan = Planner(world(g, me, [enemy]), Profile(max_stops=1)).plan()
    assert ("chip", "c:chain", 1) in kinds(plan)
    assert plan.danger == 0.0


def test_kill_is_rewarded_and_removes_danger():
    g = open_grid(16, 3)
    me = leek(1, cell(g, 4, 1))
    enemy = leek(2, cell(g, 8, 1), life=20, tp=10, mp=3, enemy=True)
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert plan.kills == [2]
    assert plan.danger == 0.0


def test_two_stops_used_when_needed():
    # Deux ennemis de part et d'autre d'un mur : on ne peut tirer sur les deux que depuis deux cases différentes.
    g = open_grid(15, 7, walls=[(7, y) for y in range(0, 6)])
    me = leek(1, cell(g, 7, 6), mp=6)
    e1 = leek(2, cell(g, 3, 4), tp=0, mp=0, enemy=True)
    e2 = leek(3, cell(g, 11, 4), tp=0, mp=0, enemy=True)
    plan = Planner(world(g, me, [e1, e2]), Profile(max_stops=2)).plan()
    targets = {a.target for a in plan.actions if a.kind == "weapon"}
    assert targets == {2, 3} or sum(a.n for a in plan.actions if a.kind == "weapon") == 4


def test_budget_cutoff_still_returns_a_plan():
    g = open_grid(16, 5)
    me = leek(1, cell(g, 3, 2))
    enemy = leek(2, cell(g, 8, 2), tp=10, mp=3, enemy=True)
    w = world(g, me, [enemy], ops=lambda: 999_999)
    planner = Planner(w, Profile())
    plan = planner.plan()
    assert planner.evaluations == 1
    assert any(a.kind == "weapon" for a in plan.actions)
    d = Danger(w)
    assert plan.danger == d.at(plan.end_cell)


def test_shield_cast_when_ending_in_danger():
    # Ennemi hors de ma portée mais moi dans la sienne partout : rien à attaquer, on doit au moins se protéger.
    from skills import REL_SHIELD
    g = open_grid(12, 3)
    fortress = make("c:fortress", REL_SHIELD, cost=6, min_range=0, max_range=0, min_v=40, max_v=40)
    me = leek(1, cell(g, 0, 1), mp=2, skills=[fortress])
    sniper = make("w:sniper", DAMAGE, cost=5, min_range=1, max_range=12, min_v=60, max_v=80, max_uses=2, is_weapon=True)
    enemy = leek(2, cell(g, 11, 1), tp=10, mp=3, enemy=True, skills=[sniper])
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert ("chip", "c:fortress", 1) in kinds(plan)


def test_no_shield_when_ending_safe():
    from skills import REL_SHIELD
    g = open_grid(30, 3)
    fortress = make("c:fortress", REL_SHIELD, cost=6, min_range=0, max_range=0, min_v=40, max_v=40)
    me = leek(1, cell(g, 0, 1), skills=[fortress])
    enemy = leek(2, cell(g, 29, 1), tp=10, mp=3, enemy=True)
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert ("chip", "c:fortress", 1) not in kinds(plan)


def test_approach_instead_of_fleeing_when_safe():
    # Ennemi loin (zone = 3 PM + 7 de portée = 10) : rien à faire ce tour, on se rapproche sans entrer dans la zone.
    g = open_grid(30, 3)
    me = leek(1, cell(g, 2, 1), mp=6)
    enemy = leek(2, cell(g, 24, 1), tp=10, mp=3, enemy=True)
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert plan.danger == 0.0
    assert g.dist(plan.end_cell, enemy.cell) < g.dist(me.cell, enemy.cell)
    assert g.dist(plan.end_cell, enemy.cell) > 10


def test_stops_at_the_edge_of_enemy_zone():
    g = open_grid(30, 3)
    me = leek(1, cell(g, 2, 1), mp=6)
    enemy = leek(2, cell(g, 16, 1), tp=10, mp=3, enemy=True)  # distance 14, zone 10 : on peut aller jusqu'à 11
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert plan.danger == 0.0
    assert g.dist(plan.end_cell, enemy.cell) == 11


def test_prebuff_shield_when_enemy_can_teleport():
    from skills import REL_SHIELD
    g = open_grid(40, 3)
    fortress = make("c:fortress", REL_SHIELD, cost=6, min_range=0, max_range=0, min_v=40, max_v=40, turns=3)
    me = leek(1, cell(g, 0, 1), mp=0, skills=[PISTOL, fortress])
    far = leek(2, cell(g, 30, 1), tp=10, mp=3, enemy=True)  # distance 30 > 3 + 12 + 7 : aucun engagement possible
    assert ("chip", "c:fortress", 1) not in kinds(Planner(world(g, me, [far]), Profile()).plan())
    tp_enemy = leek(2, cell(g, 18, 1), tp=10, mp=3, enemy=True, skills=[PISTOL, TELEPORT_CHIP])  # 18 ≤ 22
    assert ("chip", "c:fortress", 1) in kinds(Planner(world(g, me, [tp_enemy]), Profile()).plan())


def test_strength_prebuff_before_contact():
    from skills import BUFF_STRENGTH
    g = open_grid(30, 3)
    protein = make("c:protein", BUFF_STRENGTH, cost=3, min_range=0, max_range=0, min_v=100, max_v=100, turns=2,
                   raw=True)
    me = leek(1, cell(g, 0, 1), mp=3, skills=[PISTOL, protein])
    enemy = leek(2, cell(g, 12, 1), tp=10, mp=0, enemy=True)  # 12 − 3 = 9 > 7 : pas d'attaque possible ce tour
    plan = Planner(world(g, me, [enemy]), Profile()).plan()
    assert not any(a.kind == "weapon" for a in plan.actions)
    assert ("chip", "c:protein", 1) in kinds(plan)


def test_shield_stacking_has_diminishing_returns():
    # Trois boucliers relatifs disponibles, ennemi menaçant : avec w_stack bas on n'en pose pas trois.
    from skills import BUFF_MAGIC, POISON, REL_SHIELD
    g = open_grid(12, 3)
    walls = [make(f"c:wall{i}", REL_SHIELD, cost=3, min_range=0, max_range=0, min_v=30, max_v=30, turns=2)
             for i in range(3)]
    wizardry = make("c:wizardry", BUFF_MAGIC, cost=6, min_range=0, max_range=0, min_v=150, max_v=170, turns=2,
                    raw=True)
    toxin = make("c:toxin", POISON, cost=5, min_range=1, max_range=7, min_v=25, max_v=35, turns=3)
    # 9 PT : trois murs (3 PT) OU un mur + wizardry (6 PT).
    me = leek(1, cell(g, 0, 1), tp=9, mp=0, magic=100, skills=[toxin, wizardry, *walls])
    sniper = make("w:sniper", DAMAGE, cost=5, min_range=1, max_range=12, min_v=60, max_v=80, max_uses=2, is_weapon=True)
    enemy = leek(2, cell(g, 11, 1), tp=10, mp=3, enemy=True, skills=[sniper])
    plan_all = Planner(world(g, me, [enemy]), Profile(w_stack=1.0)).plan()
    plan_stack = Planner(world(g, me, [enemy]), Profile(w_stack=0.3)).plan()
    n_all = sum(1 for a in plan_all.actions if a.skill and a.skill.kind == REL_SHIELD)
    n_stack = sum(1 for a in plan_stack.actions if a.skill and a.skill.kind == REL_SHIELD)
    assert n_all == 3
    assert n_stack == 1
    assert ("chip", "c:wizardry", 1) in kinds(plan_stack)  # les PT libérés vont au buff de magie (poison)


def test_hit_and_hide_behind_obstacle():
    # Mur en x=10 (y=2..4). Je tire depuis (11,3) puis me cache en (9,3) : l'ennemi (immobile, portée 12)
    # ne voit plus la case → danger raffiné nul.
    g = open_grid(20, 7, walls=[(10, 2), (10, 3), (10, 4)])
    me = leek(1, cell(g, 11, 3), mp=6)
    sniper = make("w:sniper", DAMAGE, cost=5, min_range=1, max_range=12, min_v=60, max_v=80, max_uses=2, is_weapon=True)
    enemy = leek(2, cell(g, 18, 3), tp=10, mp=0, enemy=True, skills=[sniper])
    w = world(g, me, [enemy])
    plan = Planner(w, Profile(max_stops=1)).plan()
    assert sum(a.n for a in plan.actions if a.kind == "weapon") == 4
    assert plan.danger == 0.0
    assert not w.los(enemy.cell, plan.end_cell)
