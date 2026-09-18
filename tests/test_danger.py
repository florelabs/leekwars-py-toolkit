from danger import Danger, best_spend
from scenario import PISTOL, cell, leek, open_grid, world
from skills import DAMAGE, make


def test_best_spend_respects_uses():
    assert best_spend([(3, 10.0, 4)], 20) == 40.0  # 4 usages max
    assert best_spend([(3, 10.0, 0)], 20) == 60.0  # illimité : 6 × 3 PT
    assert best_spend([(3, 10.0, 4), (5, 20.0, 1)], 11) == 40.0  # 2 pistolets + rien : 6 PT... vs 1 gros + 2 = 40


def test_field_decreases_with_distance():
    g = open_grid(20, 5)
    me = leek(1, cell(g, 0, 2), strength=0)
    sniper = make("w:x", DAMAGE, cost=5, min_range=1, max_range=3, min_v=10, max_v=10, max_uses=2, is_weapon=True)
    enemy = leek(2, cell(g, 12, 2), tp=10, mp=2, strength=0, enemy=True, skills=[sniper])
    w = world(g, me, [enemy])
    d = Danger(w)
    assert d.at(cell(g, 12, 2)) == 20.0  # à côté : 2 tirs
    assert d.at(cell(g, 7, 2)) == 20.0  # distance 5 = 2 PM + portée 3
    assert d.at(cell(g, 6, 2)) == 0.0  # distance 6 : hors d'atteinte
    assert d.at(cell(g, 0, 2)) == 0.0


def test_shackled_variant_reduces_reach():
    g = open_grid(20, 5)
    me = leek(1, cell(g, 0, 2))
    enemy = leek(2, cell(g, 12, 2), tp=10, mp=3, enemy=True, skills=[PISTOL])
    d = Danger(world(g, me, [enemy]))
    far = cell(g, 2, 2)  # distance 10 = 3 PM + 7 de portée
    assert d.at(far) > 0
    assert d.at(far, {2: ("mp", 2.0)}) == 0.0
