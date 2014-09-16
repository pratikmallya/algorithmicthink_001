"""
implement bfs_visited, which gives the set of nodes visited by bfs
on an undirected graph starting from a specified node.

The check for whether a node has already been visited might affect
the complexity of the problem. If its O(1), its all good. Otherwise,
that complexity will be a multiple of that. i.e if its O(logn), then
time complexity of bfs will be O(nlogn).
"""

from collections import deque
import unittest


class TestAlg(unittest.TestCase):

    def test_1(self):
        EX_GRAPH2 = {
             0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])
        }
        self.assertEqual(set(range(8)), bfs_visited(EX_GRAPH2, 0))
        self.assertEqual(set(range(10)) - set([8]), bfs_visited(EX_GRAPH2, 9))
        self.assertEqual(set(range(9)) - set([0, 4, 5]), bfs_visited(EX_GRAPH2, 8))


def bfs_visited(ugraph, start_node):
    """return the set of all node visited by bfs traversal of graph"""
    neighbors = deque(neighbor for neighbor in ugraph[start_node])
    visited = set([start_node])

    while neighbors:
        node = neighbors.popleft()
        if node in visited:
            continue
        visited.add(node)
        for item in ugraph[node]:
            neighbors.append(item)

    return visited


if __name__ == "__main__":
    unittest.main()
