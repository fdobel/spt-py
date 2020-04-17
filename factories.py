from benchmark import GridGraph


def dist_foo(v, w):
    if (v, w) in [((0, 0), (1, 0)), ((1, 0), (1, 1))]:
        return 0.5
    else:
        return 1.1


grid_graph = GridGraph(3, 7, dist_foo)
