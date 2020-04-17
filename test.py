from tree import NodeBuilder
from shortest_paths import ShortestPathTree

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        bld = NodeBuilder()

        self.root1 = bld.mid(
          bld.leaf("0"),
          bld.leaf("1")
        )
        self.spt = ShortestPathTree(self.root1, depth=1)

        self.root2 = bld.mid(
          bld.mid(
            bld.leaf("0"),
            bld.leaf("1")
          ),
          bld.mid(
            bld.leaf("2"),
            bld.leaf("3")
          )
        )

        self.spt2 = ShortestPathTree(self.root2, depth=2)

    def test_case_1_output(self):
        self.assertEqual(str(self.root1), "<<e-0->:<0>> -  - <e-0->:<1>>>")

    def test_case_1(self):
        self.assertEqual([a for a in self.spt.find_leaf(0)], ['left'])

    def test_case_2(self):
        self.assertEqual([a for a in self.spt2.find_leaf(2)], ['right', 'left'])

    def test_case_2_output(self):
        self.assertEqual(str(self.root2), "<<e-0->:<<e-0->:<0>> -  - <e-0->:<1>>>> -  - <e-0->:<<e-0->:<2>> -  - <e-0->:<3>>>>>")
