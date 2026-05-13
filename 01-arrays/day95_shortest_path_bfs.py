"""
Day 95: Shortest Path in Unweighted Graph using BFS
"""

from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start):

        distance = {}
        visited = set()

        queue = deque([start])

        visited.add(start)
        distance[start] = 0

        while queue:

            node = queue.popleft()

            for neighbor in self.graph[node]:

                if neighbor not in visited:

                    visited.add(neighbor)

                    distance[neighbor] = distance[node] + 1

                    queue.append(neighbor)

        return distance


# Test
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("Shortest Distances:")
print(g.shortest_path(0))