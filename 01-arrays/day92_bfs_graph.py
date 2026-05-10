"""
Day 92: BFS Traversal of Graph
"""

from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):

        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:

            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Test
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("BFS Traversal:")
g.bfs(0)