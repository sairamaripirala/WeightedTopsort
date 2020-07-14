import unittest

from weighted_topsort import TopSort


class Testing(unittest.TestCase):
    def test_weighted_topsort(self):
        graph = {'A': 'C', 'B': '', 'C': 'D',
                 'D': '', 'E': 'C'}
        weights = [{'A': 10, 'B': 5, 'C': 17, 'D': 10, 'E': 10},
                   {'A': 10, 'B': 5, 'C': 17, 'D': 10, 'E': 5},
                   {'A': 10, 'B': 25, 'C': 17, 'D': 10, 'E': 10}]

        self.expected = [['B', 'D', 'C', 'A', 'E'],
                         ['B', 'D', 'C', 'E', 'A'],
                         ['D', 'C', 'A', 'E', 'B']]

        results = []
        for w in weights:
            r = TopSort(graph, w)
            results.append(r)
        for ex, res in zip(results, self.expected):
            self.assertEqual(list(res), list(ex))
