from tree import NodeBuilder
from run import ShortestPathTree

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        bld = NodeBuilder()

        root = bld.mid(
          bld.leaf("0"),
          bld.leaf("1")
        )
        self.spt = ShortestPathTree(root, depth=1)

        root2 = bld.mid(
          bld.mid(
            bld.leaf("0"),
            bld.leaf("1")
          ),
          bld.mid(
            bld.leaf("2"),
            bld.leaf("3")
          )
        )

        self.spt2 = ShortestPathTree(root, depth=2)

    def test_case_1(self):
        self.assertEqual([a for a in self.spt.find_leaf(0)], ['left'])

    def test_case_2(self):
        self.assertEqual([a for a in self.spt2.find_leaf(2)], ['right', 'left'])
