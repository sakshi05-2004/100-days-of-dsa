"""
Day 94: Detect Cycle in Undirected Graph
"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

    def has_cycle(self):

        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for neighbor in self.graph[node]:

                if neighbor not in visited:

                    if dfs(neighbor, node):
                        return True

                elif neighbor != parent:
                    return True

            return False

        for node in self.graph:

            if node not in visited:

                if dfs(node, -1):
                    return True

        return False


# Test
g = Graph()

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

print("Cycle Exists:", g.has_cycle())