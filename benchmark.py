

import itertools


class GridGraph:
    def __init__(self, maxrow, maxcol):
        self._nodes = [(row, col) for row, col in itertools.product(range(maxrow), range(maxcol))]
        self._maxrow = maxrow
        self._maxcol = maxcol
        # self._edges = edges

    @property
    def nodes(self):
        return self._nodes

    def edges_of(self, node):
        row, col = node
        if col + 1 < self._maxcol:
            yield (row, col + 1), 1
        if row + 1 < self._maxrow:
            yield (row + 1, col), 1
        if row + 1 < self._maxrow and col + 1 < self._maxcol:
            yield (row + 1, col + 1), 1

    def input_nodes_of(self, node):
        (row, col) = node

        if row-1 >= 0:
            yield (row-1, col)
        if col - 1 >= 0:
            yield (row, col-1)
        if row-1 >= 0 and col-1 >= 0:
            yield (row-1, col-1)

    def input_edges_of(self, node):
        for n in self.input_nodes_of(node):
            yield n, self.weight_of(n, node)

    def weight_of(self, from_n, to_n):
        return list(filter(lambda x: x[0] == to_n, self.edges_of(from_n)))[0][1]

    def __iter__(self):
        for n in self._nodes:
            yield n, list(self.edges_of(n)), list(self.input_edges_of(n))



def build_grid_graph(rows=3, cols=4):
    nodes = [(row, col) for row, col in itertools.product(range(rows), range(cols))]
    # edges = {(row, col): build_edges(row, col, rows, cols) for row, col in nodes}

    return GridGraph(rows, cols)


if __name__ == '__main__':
    gg = build_grid_graph()
    for n, out, inp in gg:
        print(n, out, inp)


