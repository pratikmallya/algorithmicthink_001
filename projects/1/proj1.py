"""
Solution to Project 1 - Degree distributions for graphs
https://class.coursera.org/algorithmicthink-001/wiki/graph_degree
"""

import unittest
from itertools import izip


EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """return complete graph with n nodes"""

    graph = {}

    for index in range(num_nodes):
        neighbor_nodes = range(num_nodes)
        neighbor_nodes.pop(index)
        graph[index] = set(neighbor_nodes)

    return graph


def compute_in_degrees(digraph):
    """return a dictionary with in-degrees of all nodes"""

    in_degrees = dict.fromkeys(digraph.keys(), 0)

    for heads in digraph.values():
        for head in heads:
            in_degrees[head] += 1

    return in_degrees


def in_degree_distribution(digraph):
    """return un-normalized distribution of in_degrees"""

    in_degrees = compute_in_degrees(digraph)
    in_degree_dist = dict.fromkeys(in_degrees.values(), 0)

    for in_degree in in_degrees.values():
        in_degree_dist[in_degree] += 1

    return in_degree_dist


class TestAlg(unittest.TestCase):
    """Unit test class to test algorithms"""

    def test_make_complete_graph(self):
        """Test the make_complete_graph function"""

        n = 100
        graph = make_complete_graph(n)

        for node, neighbors in graph.items():
            real_neighbors = range(n)
            real_neighbors.pop(node)
            self.assertEqual(set(real_neighbors), neighbors)

    def test_compute_in_degrees(self):
        """Test the compute_in_degrees function"""

        computed_indegs = [compute_in_degrees(EX_GRAPH0),
                           compute_in_degrees(EX_GRAPH1),
                           compute_in_degrees(EX_GRAPH2)]

        indegs = [{0: 0, 1: 1, 2: 1},
                  {0: 1, 1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1},
                  {0: 1, 1: 3, 2: 3, 3: 3, 4: 2, 5: 2, 6: 2, 7: 3, 8: 0,
                   9: 0}]

        for computed_indeg, indeg in izip(computed_indegs, indegs):
            self.assertEqual(computed_indeg, indeg)

    def test_in_degree_distribution(self):
        """Test the in_degree_distribution function"""

        c_indeg_dists = [in_degree_distribution(EX_GRAPH0),
                         in_degree_distribution(EX_GRAPH1),
                         in_degree_distribution(EX_GRAPH2)]

        indeg_dists = [{0: 1, 1: 2},
                       {1: 5, 2: 2},
                       {0: 2, 1: 1, 2: 3, 3: 4}]

        for c_indeg_dist, indeg_dist in izip(c_indeg_dists, indeg_dists):
            self.assertEqual(c_indeg_dist, indeg_dist)


if __name__ == "__main__":
    unittest.main()
