
from spt.shortest_path_tree import ShortestPathTree


class ShortestPaths:

    def __init__(self):
        self._dists = {}

    def set(self, v, w, dist):
        self._dists[(v, w)] = dist

    def dist(self, v, w):
        return self._dists[(v, w)]

