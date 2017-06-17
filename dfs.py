from collections import defaultdict
# DFS


class Vertex:

    def __init__(self, i):
        self.name = i
        self.n = None
        self.color = None
        self.parent = None
        self.first = None


class DFSVertex(Vertex):

    def __init__(self, i):
        super().__init__(i)
        self.d = 0
        self.f = 0


class DFS:

    def __init__(self, connections):
        self.time = 0
        self.vertices = list({a for a, b in connections} | {b for a, b in connections})
        self.adj = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self.adj[node1].add(node2)

    def dfs(self):
        for u in self.vertices:
            u.color = "W"
            u.parent = -1
        self.time = 0
        for u in self.vertices:
            if u.color == "W":
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        u.d = self.time
        u.color = "G"
        v = u.first
        while v:
            if self.vertices[v.n].color == "W":
                self.vertices[v.n].parent = u.n
                self.dfs_visit(self.vertices[v.n])
            v = v.next
        u.color = "B"
        self.time += 1
        u.f = self.time


a = DFSVertex("a")
b = DFSVertex("b")
c = DFSVertex("c")
d = DFSVertex("d")
e = DFSVertex("e")
f = DFSVertex("f")
g = DFSVertex("g")
h = DFSVertex("h")
connections = [(a, b), (b, c), (b, e), (b, f), (c, d), (c, g), (d, c), (d, h), (e, a), (e, f), (f, g), (g, f), (g, h), (h, h)]
g = DFS(connections)
g.dfs()


# def remove(self, node):
#     """ Remove all references to node """

#     for n, cxns in self._graph.iteritems():
#         try:
#             cxns.remove(node)
#         except KeyError:
#             pass
#     try:
#         del self._graph[node]
#     except KeyError:
#         pass

# def is_connected(self, node1, node2):
#     """ Is node1 directly connected to node2 """

#     return node1 in self._graph and node2 in self._graph[node1]

# def find_path(self, node1, node2, path=[]):
#     """ Find any path between node1 and node2 (may not be shortest) """

#     path = path + [node1]
#     if node1 == node2:
#         return path
#     if node1 not in self._graph:
#         return None
#     for node in self._graph[node1]:
#         if node not in path:
#             new_path = self.find_path(node, node2, path)
#             if new_path:
#                 return new_path
#     return None

# def __str__(self):
#     return '{}({})'.format(self.__class__.__name__, dict(self._graph))
