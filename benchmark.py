

import itertools


class GridGraph:
    def __init__(self, maxrow, maxcol, weight_function):
        self._nodes = [(row, col) for row, col in itertools.product(range(maxrow), range(maxcol))]
        self._maxrow = maxrow
        self._maxcol = maxcol
        self._weight_function = weight_function

    @property
    def nodes(self):
        return self._nodes

    def weight(self, v, w):
        return self._weight_function(v, w)

    def edges_of(self, node):
        row, col = node
        if col + 1 < self._maxcol:
            out = (row, col + 1)
            yield out, self.weight(node, out)
        if row + 1 < self._maxrow:
            out = (row + 1, col)
            yield out, self.weight(node, out)
        if row + 1 < self._maxrow and col + 1 < self._maxcol:
            out = (row + 1, col + 1)
            yield out, self.weight(node, out)

    def input_nodes_of(self, node):
        row, col = node

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

    def __str__(self):
        s = ""
        crow = 0
        ws = ""
        for (r, c), oue, _2 in self:
            rw, cw, dw = "", "", ""

            same_row_node = list(filter(lambda x: x[0][0] == r, oue))
            if len(same_row_node) >= 1:
                rw = same_row_node[0][1]

            same_col_node = list(filter(lambda x: x[0][1] == c, oue))
            if len(same_col_node) >= 1:
                cw = same_col_node[0][1]

            diag_node = list(filter(lambda x: x[0][0] == r+1 and x[0][1] == c+1, oue))
            if len(diag_node) >= 1:
                dw = diag_node[0][1]

            if r > crow:
                crow = r
                s += "\n" + ws + \
                     "\n"
                ws = ""

            uws = "| %s \\ %s " % ("{:<6s}".format(str(cw)), "{:<6s}\\".format(str(dw)))

            ws += uws

            if c >= self._maxcol-1:
                s += "-o"
            else:
                s += "o----[%6.1f]------" % (rw)
        return s


class WeightBuilder:
    def __init__(self):
        pass

    def build(self):
        return lambda x, y: 1


class GridBuilder:
    def __init__(self):
        self._rows = None
        self._cols = None

        self._weight_builder = WeightBuilder()

    def rows(self, r):
        self._rows = r
        return self

    def cols(self, c):
        self._cols = c
        return self

    def build(self):
        weights = self._weight_builder.build()
        return GridGraph(self._rows, self._cols, weights)


def build_grid_graph(rows=3, cols=4):
    return GridBuilder().rows(rows).cols(cols).build()


if __name__ == '__main__':
    gg = build_grid_graph()
    for n, out, inp in gg:
        print(n, out, inp)


