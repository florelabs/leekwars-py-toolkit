from geometry import LAUNCH_LINE, Grid, bfs_walk, dist_field
from scenario import cell, open_grid


def test_ring_and_launch():
    g = open_grid(9, 9)
    c = cell(g, 4, 4)
    ring = g.ring(c, 1, 2)
    assert len(ring) == 12  # 4 à distance 1, 8 à distance 2
    line = g.ring(c, 1, 3, LAUNCH_LINE)
    assert len(line) == 12 and all(g.xy[x][0] == 4 or g.xy[x][1] == 4 for x in line)


def test_bfs_walk_blocked_and_dist_field():
    g = open_grid(7, 7, walls=[(3, y) for y in range(0, 6)])  # mur vertical avec un trou en bas
    start = cell(g, 1, 3)
    reach = bfs_walk(g, {start: 0}, 4, list(g.obstacle))
    assert cell(g, 4, 3) not in reach  # derrière le mur, trop loin par le trou
    assert reach[cell(g, 1, 6)] == 3
    field = dist_field(g, [start])
    assert field[cell(g, 4, 3)] == 3  # le champ de distance ignore les obstacles


def test_from_ascii_los():
    g = Grid.from_ascii(["....", ".#..", "...."])
    blocked = list(g.obstacle)
    assert not g.los_ascii(cell(g, 0, 1), cell(g, 3, 1), blocked)
    assert g.los_ascii(cell(g, 0, 0), cell(g, 3, 0), blocked)
