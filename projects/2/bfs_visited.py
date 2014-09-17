"""
implement bfs_visited, which gives the set of nodes visited by bfs
on an undirected graph starting from a specified node.

The check for whether a node has already been visited might affect
the complexity of the problem. If its O(1), its all good. Otherwise,
that complexity will be a multiple of that. i.e if its O(logn), then
time complexity of bfs will be O(nlogn).
"""

from collections import deque


def bfs_visited(ugraph, start_node):
    """compute set of all node visited by bfs traversal of graph"""
    neighbors = deque([start_node])
    visited = set()

    while neighbors:
        node = neighbors.popleft()
        visited.add(node)
        for item in ugraph[node]:
            if item not in visited:
                neighbors.append(item)

    return visited


def cc_visited(ugraph):
    """compute connected components of graph"""
    connected_components = []
    allnodes = set(ugraph.keys())

    while allnodes:
        node = allnodes.pop()
        visited = bfs_visited(ugraph, node)
        allnodes -= visited
        connected_components.append(visited)

    return connected_components


def largest_cc_size(ugraph):
    """compute the size of the largest connected component"""

    connected_components = cc_visited(ugraph)
    if connected_components:
        return len(max(connected_components))
    else:
        return 0

def compute_resilience(ugraph, attack_order):
    """compute the resilience of the graph given attack order"""
    resilience = [largest_cc_size(ugraph)]

    for node in attack_order:
        remove_node(ugraph, node)
        resilience.append(largest_cc_size(ugraph))

    return resilience


def remove_node(ugraph, node):
    """remove node from graph"""

    neighbors = ugraph[node]
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    del ugraph[node]
