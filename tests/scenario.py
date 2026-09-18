# Fabrique de scénarios synthétiques pour les tests : grille ASCII, entités, skills.

from geometry import Grid
from skills import DAMAGE, make
from world import Ent, World

PISTOL = make("w:pistol", DAMAGE, cost=3, min_range=1, max_range=7, min_v=15, max_v=20, max_uses=4, is_weapon=True)


def open_grid(w: int = 12, h: int = 12, walls: list[tuple[int, int]] | None = None) -> Grid:
    rows = [["."] * w for _ in range(h)]
    for x, y in walls or []:
        rows[y][x] = "#"
    return Grid.from_ascii(["".join(r) for r in rows])


def cell(grid: Grid, x: int, y: int) -> int:
    return grid.by_xy[(x, y)]


def leek(eid: int, c: int, *, life: int = 1000, tp: int = 20, mp: int = 6, strength: int = 100, enemy: bool = False,
         skills=None, **kw) -> Ent:
    return Ent(id=eid, cell=c, life=life, max_life=kw.pop("max_life", life), tp=tp, mp=mp, strength=strength,
               enemy=enemy, skills=list(skills or [PISTOL]), weapon_key="w:pistol", **kw)


def world(grid: Grid, me: Ent, enemies: list[Ent], los: bool = True, ops=None, max_ops: int = 1_000_000) -> World:
    w = World(grid=grid, me=me, enemies=enemies, max_ops=max_ops)
    if los:
        blocked = w.blocked
        w.los = lambda a, b: grid.los_ascii(a, b, blocked)
    if ops is not None:
        w.ops = ops
    return w
