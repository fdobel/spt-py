from spt.iter_leaf_indices import distance_common_ancestor, nav_tree_node_to_node, walk_tree
from spt.merge_tree import merge_binary_tree_along_path_to_leaf, MergeInfo
from spt.tree import NodeBuilder

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        b = NodeBuilder()

        self.m1 = b.mid(
            b.mid(b.leaf("0"), b.leaf("1"), lw=3, rw=2),
            b.mid(b.leaf("2"), b.leaf("3"), lw=4, rw=5),
            lw=1, rw=0
        )

        self.m2 = b.mid(
            b.mid(b.leaf("x0"), b.leaf("x1")),
            b.mid(b.leaf("x2"), b.leaf("x3"))
        )

    def test_case_1(self):
        self.assertEqual(
            [a for a in map(lambda x: x[0], walk_tree(self.m1, [1, 3]))],
            ['left', 'right', 'up', 'up', 'right', 'right']
        )

    def test_case_2(self):
        self.assertEqual(
            [a for a in map(lambda x: x[0], walk_tree(self.m1, [1, 3, 2]))],
            ['left', 'right', 'up', 'up', 'right', 'right', 'up', 'left']
        )

    def test_case_3(self):
        self.assertEqual(
            [a for a in map(lambda x: x[0], walk_tree(self.m1, [0, 1, 3, 2]))],
            ['left', 'left', 'up', 'right', 'up', 'up', 'right', 'right', 'up', 'left']
        )
