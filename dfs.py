from collections import defaultdict
# DFS


class Vertex():

    def __init__(self, i):
        self.name = i
        self.color = None
        self.pre = None


class DFSVertex(Vertex):

    def __init__(self, i):
        super().__init__(i)
        self.d = 0
        self.f = 0


class DFS():

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
            u.pre = None
        self.time = 0
        for u in self.vertices:
            if u.color == "W":
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        u.d = self.time
        u.color = "G"
        for v in self.adj[u]:
            if v.color == "W":
                v.pre = u.name
                self.dfs_visit(v)
        u.color = "B"
        self.time += 1
        u.f = self.time

    # def scc(self):
    #     self.dfs()
    #     self.transpose()
    #     sorted = self.sort_by_f()
    #     vset = self.vertices
    #     for v in vset:
    #         v.color = "W"
    #         v.pre = -1
    #     for n in sorted:
    #         if self.vertices[n].color == "W":
    #             self.scc_find(vset[n])

a = DFSVertex("a")
b = DFSVertex("b")
c = DFSVertex("c")
d = DFSVertex("d")
e = DFSVertex("e")
f = DFSVertex("f")
g = DFSVertex("g")
h = DFSVertex("h")
connections = [(a, b), (b, c), (b, e), (b, f), (c, d), (c, g), (d, c), (d, h), (e, a), (e, f), (f, g), (g, f), (g, h), (h, h)]
dfs = DFS(connections)
dfs.dfs()
print([i.name for i in dfs.vertices])
for u in dfs.vertices:
    print(u.name, u.color, u.pre, u.d, u.f, [i.name for i in dfs.adj[u]])
