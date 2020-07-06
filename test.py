import unittest

from weighted_topsort import WeightedTopsort


class Testing(unittest.TestCase):
    def test_weighted_topsort(self):
        graph = {"A": "C", "B": "", "C": "D",
                 "D": "", "E": "C"}
        weights = {'A': 10, 'B': 5, 'C': 17, 'D': 10, 'E': 10}
        self.expected = ['B', 'D', 'C', 'A', 'E']
        result = WeightedTopsort(graph, weights)
        self.assertEqual(
            [i for i in result],
            [i for i in self.expected])
