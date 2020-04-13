"""
Simple graph implementation
"""

from util import Stack, Queue  # These may come in handy
from typing import List


class Graph:
    def __init__(self):
        """Represent a graph as a dictionary of vertices mapping labels to edges."""
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """Add a vertex to the graph."""
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """Add a directed edge to the graph, from v1 to v2."""
        # Check if exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print(f"Error: Vertex not found")

    def get_neighbors(self, vertex_id):
        """Get all neighbors (edges) of a vertex."""
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, start_vertex):
        """Print each vertex in breadth-first order
        beginning from start_vertex.
        """
        # Create a q and n q starting vertex
        qq = Queue()
        qq.enqueue([start_vertex])
        # Create set of traversed vertices
        visited = set()
        # While queue is not empty
        while qq.size() > 0:
            # Dequeue first vertex
            path = qq.dequeue()
            # If not in traversed
            if path[-1] not in visited:
                # DO THE THANG
                print(path[-1])
                # Mark as visited
                visited.add(path[-1])
                # Enqueue all neighbors
                for ngbr in self.get_neighbors(path[-1]):
                    new_path = path + [ngbr]
                    qq.enqueue(new_path)

    def dft(self, start_vertex):
        """Print each vertex in depth-first order
        beginning from start_vertex.
        """
        # Create stack and push starting vertex
        stack = Stack()
        stack.push([start_vertex])
        # Create set of traversed vertices
        visited = set()
        # While stack is not empty
        while stack.size() > 0:
            # Pop first vertex
            path = stack.pop()
            # If not in traversed
            if path[-1] not in visited:
                # DO THE THANG
                print(path[-1])
                # Mark as visited
                visited.add(path[-1])
                # Push all neighbors
                for ngbr in self.get_neighbors(path[-1]):
                    new_path = path + [ngbr]
                    stack.push(new_path)

    def dft_recursive(self, start_vertex):
        """Print each vertex in depth-first order
        beginning from start_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, start_vertex, dst_vertex):
        """Return a list containing the shortest path from
        start_vertex to dst_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, start_vertex, dst_vertex):
        """Return a list containing a path from
        start_vertex to dst_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, start_vertex, dst_vertex):
        """Return a list containing a path from
        start_vertex to dst_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
