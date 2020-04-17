from spt.iter_leaf_indices import distance_common_ancestor
from spt.merge_tree import merge_binary_tree_along_path_to_leaf, MergeInfo
from spt.tree import NodeBuilder

import unittest


class Test(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(distance_common_ancestor(3, 4, 7), 2)

    def test_case_2(self):
        self.assertEqual(distance_common_ancestor(3, 1, 7), 3)

    def test_case_3(self):
        self.assertEqual(distance_common_ancestor(3, 3, 7), 3)

    def test_case_4(self):
        self.assertEqual(distance_common_ancestor(3, 0, 7), 3)

    def test_case_5(self):
        self.assertEqual(distance_common_ancestor(4, 0, 15), 4)

    def test_case_6(self):
        self.assertEqual(distance_common_ancestor(4, 4, 5), 1)

    def test_case_7(self):
        self.assertEqual(distance_common_ancestor(5, 3, 4), 3)