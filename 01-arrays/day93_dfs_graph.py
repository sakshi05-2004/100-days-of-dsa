"""
Day 93: DFS Traversal of Graph
"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited=None):

        if visited is None:
            visited = set()

        visited.add(node)

        print(node, end=" ")

        for neighbor in self.graph[node]:

            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Test
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("DFS Traversal:")
g.dfs(0)