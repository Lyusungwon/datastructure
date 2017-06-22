from collections import defaultdict
# BFS


class Vertex():

    def __init__(self, i):
        self.name = i
        self.color = None
        self.pre = None


class BFSVertex(Vertex):

    def __init__(self, i):
        super().__init__(i)
        self.d = 0


class BFS():

    def __init__(self, connections):
        self.time = 0
        self.vertices = {a for a, b in connections} | {b for a, b in connections}
        self.adj = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self.adj[node1].add(node2)

    def bfs(self, s):
        for u in self.vertices - {s}:
            u.color = "W"
            u.d = float("inf")
            u.pre = None
        s.color = "G"
        s.d = 0
        s.pre = None
        q = []
        q.append(s)
        while len(q) != 0:
            u = q.pop()
            for v in self.adj[u]:
                if v.color == "W":
                    v.color = "G"
                    v.d = u.d + 1
                    v.pre = u
                    q.append(v)
            u.color = "B"
            print(u.name, u.color, u.d)


a = BFSVertex("a")
b = BFSVertex("b")
c = BFSVertex("c")
d = BFSVertex("d")
e = BFSVertex("e")
f = BFSVertex("f")
g = BFSVertex("g")
h = BFSVertex("h")
connections = [(a, b), (b, c), (b, e), (b, f), (c, d), (c, g), (d, c), (d, h), (e, a), (e, f), (f, g), (g, f), (g, h), (h, h)]
bfs = BFS(connections)
bfs.bfs(a)
