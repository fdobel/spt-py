

import unittest

from spt.operations.constructions import construction0, construction1, single_node_at
from spt.tree import NodeBuilder


class Test(unittest.TestCase):

    def setUp(self):
        bld = NodeBuilder()
        self.r = bld.mid(
            bld.mid(bld.leaf("0"), bld.leaf("1")),
            bld.only_left_child(bld.leaf("2"))
        )

    def test_case_1(self):
        bld = NodeBuilder()
        r = bld.only_left_child(bld.leaf("0"))
        n = single_node_at(r, 1, 1, "1")
        self.assertEqual(n.depth, 1)
        self.assertEqual(str(n), "N:[e(0)=>[<0>]]-o-[e(0)=>[<1>]]")

    def test_case_3(self):
        n = single_node_at(self.r, 3, 2, "3")
        self.assertEqual(self.r.depth, 2)
        self.assertEqual(n.depth, 2)
        self.assertEqual(str(n), "N:[e(0)=>[N:[e(0)=>[<0>]]-o-[e(0)=>[<1>]]]]-o-[e(0)=>[N:[e(0)=>[<2>]]-o-[e(0)=>[<3>]]]]")

    #def test_case_4(self):
    #    b, _ = construction1(self.a, self.a.leaf_nodes)
    #    c, _ = construction1(b, b.leaf_nodes)
    #    d, _ = construction1(c, c.leaf_nodes)
    #    self.assertEqual(d.depth, 2)  # self.assertEqual(d.leaf_nodes, ["0", "1", "2", "3"])

