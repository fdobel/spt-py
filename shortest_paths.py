
from spt.shortest_path_tree import ShortestPathTree


class ShortestPaths:

    def __init__(self, source_nodes, target_nodes):
        self._dists = {}
        self._source_nodes = source_nodes
        self._target_nodes = target_nodes

    def set(self, v, w, dist):
        assert v in self._source_nodes
        # assert w in self._target_nodes

        self._dists[(v, w)] = dist

    def dist(self, v, w):
        if v == w:
            return 0.0
        return self._dists[(v, w)]

    def __str__(self):
        s = ""
        for k, v in self._dists.items():
            if k[1] in self._target_nodes:
                s += (k, v).__str__() + "\n"
        return s
