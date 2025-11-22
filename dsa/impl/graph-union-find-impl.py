# @author: yprakash
# Python Program for union-find algorithm to detect cycle in an undirected graph
# we have one edge for any two vertex i.e. 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.v = vertices # no.of vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        if u < v:
            self.graph[u].append(v)
        else:
            self.graph[v].append(u)

    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find_parent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    # The main function to check whether a given graph contains cycle or not
    def is_cyclic(self):
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1] * self.v

        # Iterate through all edges of graph, find subset of both vertices of every edge,
        # if both subsets are same, then there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True  # Cycle found in graph
                self.union(parent, x, y)


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
