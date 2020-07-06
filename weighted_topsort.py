"""
It is an implementation of Topological sort using Depth First Search.
The implementation provides a way to sort the nodes of the graph based on
the weights assigned to each node. When a node is dependent on two other nodes
the node with lowest weight is resolved first.

The input graph is a json structure with dependecies for the node are
indicated as a list. The weights for the nodes are provided as a set of
tag-value pairs.
"""

import heapq
from collections import deque


class CyclicGraphError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.errors = message


class WeightedTopsort(list):
    def __init__(self, indata, weights):
        self.data = indata
        self.weights = weights.copy()
        self.visit_stack = deque()
        self.sort_stack = deque()
        self.evaluate_nodes(self.data)

    def __iter__(self):
        return iter(self.sort_stack)

    """Resolve first level nodes of the graph
       in order of weights indicated for the nodes"""
    def evaluate_nodes(self, jsondata):
        keys_heap = [(self.weights.get(k, 1), k) for k in jsondata.keys()]
        heapq.heapify(keys_heap)
        while keys_heap:
            _, key = heapq.heappop(keys_heap)
            if not (key in self.visit_stack):
                self.visit_stack.append(key)
                if jsondata.get(key):
                    self.eval_depnds(jsondata.get(key))
                self.sort_stack.append(str(key))
        return self.sort_stack

    """Resolve the dependencies list in order of weights
       provided, lower to higher"""
    def eval_depnds(self, dep_list):
        ch_jsondata = {}
        ch_keys_heap = [(self.weights.get(k, 1), k) for k in dep_list]
        heapq.heapify(ch_keys_heap)
        while ch_keys_heap:
            _, ch_val = heapq.heappop(ch_keys_heap)
            if not (ch_val in self.visit_stack):
                if str(ch_val) in self.data.keys():
                    ch_jsondata[ch_val] = self.data.get(str(ch_val))
                    self.evaluate_nodes(ch_jsondata)
                else:
                    self.visit_stack.append(ch_val)
                    self.sort_stack.append(str(ch_val))
            elif not (ch_val in self.sort_stack):
                raise CyclicGraphError(
                    'Cycle detected for key {}'.format(str(ch_val)))


if __name__ == "__main__":
    data = {"A": "C",  "B": "", "C": "D", "D": "", "E": "C"}
    table = {'A': 10, 'B': 5, 'C': 17, 'D': 10, 'E': 10}
    print(WeightedTopsort(data, table))
