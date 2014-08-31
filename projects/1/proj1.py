import unittest


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

EX_GRAPH1 = {0: set([1, 4]),
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

    for i in range(num_nodes):
        neighbor_nodes = range(num_nodes)
        neighbor_nodes.pop(i)
        graph[i] = set(neighbor_nodes)

    return graph

def compute_in_degrees(digraph):
    """return a dictionary with in-degrees of all nodes"""

    in_degrees = dict.fromkeys(digraph.keys, 0)

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


if __name__ == "__main__":
    unittest.main()