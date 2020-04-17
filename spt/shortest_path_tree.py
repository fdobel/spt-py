class ShortestPathTree:

    def __init__(self, root, depth=None):
        self._root = root
        self._depth = depth

    @property
    def depth(self):
        return self._depth

    def find_leaf(self, leaf_idx):
        if self.depth is None:
            raise RuntimeError("depth is not set")
        mask = 1 << (self.depth - 1)

        while mask > 0:
            if mask & leaf_idx == 0:
                yield "left"
            else:
                yield "right"
            mask = mask >> 1


