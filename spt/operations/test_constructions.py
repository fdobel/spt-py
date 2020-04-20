

import unittest

from spt.operations.constructions import construction0, construction1


class Test(unittest.TestCase):

    def setUp(self):
        self.a, s = construction0("0")

    def test_case_1_output(self):
        self.assertEqual(self.a.depth, 0)
        self.assertEqual(self.a.is_leaf, True)
        self.assertEqual(self.a.name, '0')

    def test_case_2(self):
        b, _ = construction1(self.a, self.a.leaf_nodes)
        self.assertEqual(b.depth, 1)

    def test_case_2_leafs(self):
        b, _ = construction1(self.a, self.a.leaf_nodes)
        self.assertEqual(b.leaf_nodes, ["0", "1"])

    def test_case_3(self):
        b, _ = construction1(self.a, self.a.leaf_nodes)
        c, _ = construction1(b, b.leaf_nodes)
        self.assertEqual(c.depth, 2)

    def test_case_3_leaves(self):
        b, _ = construction1(self.a, self.a.leaf_nodes)
        c, _ = construction1(b, b.leaf_nodes)
        self.assertEqual(c.leaf_nodes, ["0", "1", "2"])

    def test_case_4(self):
        b, _ = construction1(self.a, self.a.leaf_nodes)
        c, _ = construction1(b, b.leaf_nodes)
        d, _ = construction1(c, c.leaf_nodes)
        self.assertEqual(d.depth, 2)  # self.assertEqual(d.leaf_nodes, ["0", "1", "2", "3"])

    def test_case_4_leaves(self):
        a = self.a
        b, _ = construction1(self.a, self.a.leaf_nodes)
        c, _ = construction1(b, b.leaf_nodes)
        d, _ = construction1(c, c.leaf_nodes)
        self.assertEqual(d.leaf_nodes, ["0", "1", "2", "3"])