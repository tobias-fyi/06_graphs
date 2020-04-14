"""
Graphs :: Day 2 Project
"""

import sys
import os

sys.path.append(os.path.abspath("../graph"))
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Instantiate graph
    graph = Graph()

    # Loop through input to add all vertices
    for rel in ancestors:  # Each element is (parent, child)
        parent = rel[0]
        child = rel[1]

        # Check for vertices in graph, adding if needed
        if parent not in graph.vertices:  # Check if parent exists
            # If parent doesn't exist, add it
            graph.add_vertex(parent)

        if child not in graph.vertices:  # Check if child exists
            # If child doesn't exist, add it
            graph.add_vertex(child)

        # Add the edge between child -> parent
        # This relation b/c direction of search is child -> parent
        graph.add_edge(child, parent)

    if len(graph.vertices[starting_node]) < 1:
        return -1
    else:
        return graph.bft(starting_node)


if __name__ == "__main__":
    # === Give 'er a little test
    test_ancestors = [
        (1, 3),
        (2, 3),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
        (8, 9),
        (11, 8),
        (10, 1),
    ]
    earliest_ancestor(test_ancestors, 2)
    earliest_ancestor(test_ancestors, 6)
