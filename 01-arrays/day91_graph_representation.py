"""
Day 91: Graph Representation using Adjacency List
"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        # Undirected graph
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):

        for node in self.graph:
            print(node, "->", self.graph[node])


# Test
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.display()