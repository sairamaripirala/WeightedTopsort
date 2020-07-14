import unittest

from weighted_topsort import CyclicGraphError, TopSort


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

    def test_cyclic_graph(self):
        graph = {'A': 'C', 'B': '', 'C': 'D',
                 'D': 'A', 'E': 'C'}
        weight = {'A': 10, 'B': 5, 'C': 17, 'D': 10, 'E': 10}
        with self.assertRaises(CyclicGraphError):
            TopSort(graph, weight)

    def test_no_depds(self):
        graph = {'A': 'C', 'B': '', 'C': 'D',
                 'D': 'F', 'E': 'C'}
        weight = {'A': 10, 'B': 5, 'C': 17, 'D': 10, 'E': 10}
        result = TopSort(graph, weight)
        self.expected = ['B', 'F', 'D', 'C', 'A', 'E']
        self.assertEqual(self.expected, list(result))
