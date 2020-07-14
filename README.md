![Testing](https://github.com/saripirala/weighted_topsort/workflows/Testing/badge.svg?branch=review)
[![Documentation Status](https://readthedocs.org/projects/weighted_topsort/badge/?version=latest)](https://weighted_topsort.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/saripirala/weighted_topsort/branch/review/graph/badge.svg)](https://codecov.io/gh/saripirala/weighted_topsort)

# WeightedTopsort
This an implementation of Topological sort using depth first search (DFS), with provision of weights/priority for nodes to be processed. There are multiple paths for a graph to be topologically sorted, this implementation allows the order to be tweaked using priority/weights to the nodes. The nodes with lowest weight is processed first.

## Usage:

    Example 1:
    >>> from weighted_topsort import TopSort
    >>> graph = {"A": "C", "B": "", "C": "D",
                 "D": "", "E": "C"}
    >>> weight={'A': 10, 'B': 5, 'C': 17, 'D': 10, 'E': 10}
    >>> result = TopSort(graph, weight)
    >>> print(list(result))
    ['B', 'D', 'C', 'A', 'E']

    Example 2:
    >>> gr={"N2": ["N11"], "N9": ["N11", "N8", "N10"],
            "N10": ["N11", "N3"], "N11": ["N7", "N5"],
            "N8": ["N7", "N3"]}
    >>> wt = {"N7": 3, "N5": 2, "N11": 1, "N2": 1, "N3": 1, "N8": 1, "N10": 1, "N9": 1}
    >>> result = TopSort(gr, wt)
    >>> print(list(result))
    ['N5', 'N7', 'N11', 'N3', 'N10', 'N2', 'N8', 'N9']

Input is a directed graph, must be a json with dependency or list of dependencies for nodes.

The weights for the nodes is also a JSON with node name as mentioned in the Graph and corresponding weight.

The result is an iteratable sroted list.
