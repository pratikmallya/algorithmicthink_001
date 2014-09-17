"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""

# general imports
import urllib2
from proj1 import compute_in_degrees, in_degree_distribution, DPA
from matplotlib import pyplot


CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def normalize_indegree_dist(graph):
    """Normalizes the indegree values of the distribution dictionary"""

    gsum = sum(graph.values())

    for node, indeg in graph.items():
        graph[node] = float(indeg)/float(gsum)

    return None


def plot_deg_dist(graph):
    """Plot the normalized indegree distribution"""

    x = graph.keys()
    x.sort()

    if x[0] == 0:
        x.pop(0)

    y = [graph[value] for value in x]

    pyplot.subplot(1,1,1)
    pyplot.plot(x, y, 'b.')
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.xlabel('$\log$(in-degree)')
    pyplot.ylabel('$\log$(no. of nodes) (normalized)')
    pyplot.title('Distribution of in-degree for DPA graph')
    pyplot.grid('on')
    pyplot.show()


def main():
    #graph = load_graph(CITATION_URL)

    graph = DPA(27770, 13)
    import cPickle as pickle

    with open("graph.pkl", 'w') as o:
        pickle.dump(graph, o)

    indeg_dist_graph = in_degree_distribution(graph)
    normalize_indegree_dist(indeg_dist_graph)
    plot_deg_dist(indeg_dist_graph)


if __name__ == "__main__":
    main()
