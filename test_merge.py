
from spt.merge_tree import merge_binary_tree_along_path_to_leaf, MergeInfo
from spt.tree import NodeBuilder

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        b = NodeBuilder()

        self.m1 = b.mid(
            b.mid(b.leaf("0"), b.leaf("1")),
            b.mid(b.leaf("2"), b.leaf("3"))
        )

        self.m2 = b.mid(
            b.mid(b.leaf("x0"), b.leaf("x1")),
            b.mid(b.leaf("x2"), b.leaf("x3"))
        )

    def test_case_1_output(self):
        result = merge_binary_tree_along_path_to_leaf(self.m1, self.m2, [MergeInfo('left', 1, 1), MergeInfo('right', 1, 1)])
        self.assertEqual(
            str(result),
            "N:[e(1)=>[N:[e(1)=>[<0>]]-o-[e(1)=>[<1>]]]]-o-[e(1)=>[N:[e(0)=>[<x2>]]-o-[e(0)=>[<x3>]]]]"
        )
    def test_case_2_output(self):
        result = merge_binary_tree_along_path_to_leaf(self.m1, self.m2, [MergeInfo('left', 1, 1), MergeInfo('right', 1, 1)], pref='right')
        self.assertEqual(
            str(result),
            "N:[e(1)=>[N:[e(1)=>[<0>]]-o-[e(1)=>[<x1>]]]]-o-[e(1)=>[N:[e(0)=>[<x2>]]-o-[e(0)=>[<x3>]]]]"
        )
