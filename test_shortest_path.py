from factories import grid_graph
from run import compute_shortest_paths
from tree import NodeBuilder
from shortest_paths import ShortestPathTree

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        source_nodes = [(0, i) for i in range(7)]
        self.tn = (2, 6)
        target_nodes = [self.tn]

        self.sp = compute_shortest_paths(grid_graph, source_nodes, target_nodes)

    def test_case_1(self):
        self.assertEqual(self.sp.dist((0, 0), self.tn), 6.5)

    def test_case_2(self):
        self.assertEqual(self.sp.dist((0, 1), self.tn), 5.5)
    def test_case_3(self):
        self.assertEqual(self.sp.dist((0, 2), self.tn), 4.4)
    def test_case_4(self):
        self.assertEqual(self.sp.dist((0, 3), self.tn), 3.3000000000000003)
    def test_case_5(self):
        self.assertEqual(self.sp.dist((0, 4), self.tn), 2.2)

    def test_case_6(self):
        self.assertEqual(self.sp.dist((0, 5), self.tn), 2.2)

    def test_case_7(self):
        self.assertEqual(self.sp.dist((0, 6), self.tn), 2.2)

