from benchmark import GridGraph


import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.grid = GridGraph(2, 2)

    def test_case_1_output(self):
        self.assertEqual([a for a in self.grid], [
            (
                (0, 0),
                [((0, 1), 1), ((1, 0), 1), ((1, 1), 1)],
                []
            ),
            (
                (0, 1),
                [((1, 1), 1)],
                [((0, 0), 1)]
            ),
            (
                (1, 0),
                [((1, 1), 1)],
                [((0, 0), 1)]
            ),
            (
                (1, 1), [], [((0, 1), 1), ((1, 0), 1), ((0, 0), 1)]
            )
        ])

