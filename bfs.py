from collections import defaultdict
# BFS


class Queue:

    def __init__(self):
        self.front = 0
        self.rear = 0
        self.sz = 0
        self.buf = []

    def create_queue(self, sz):
        self.sz = sz
        self.buf = list(range(sz))

    def enqueue(self, val):
        self.buf[self.rear] = val
        self.rear = (self.rear + 1) % self.sz

    def dequeue(self):
        res = self.buf[self.front]
        self.front = (self.front + 1) % self.sz
        return res

    def is_empty(self):
        return self.front == self.rear


class Vertex:

    def __init__(self, i):
        self.n = i
        self.color = None
        self.parent = None
        self.first = None
        self.d = None
        self.f = None


class Graph(object):

    def __init__(self, connections, directed=False):
        nil = Vertex(None)
        self.vertices = {a for a, b in connections} | {b for a, b in connections}
        self.adj = defaultdict(set)
        self.nil = nil
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self.adj[node1].add(node2)
        if not self._directed:
            self.adj[node2].add(node1)

    def bfs(self, s):
        for u in self.vertices - {s}:
            u.color = "W"
            u.d = float("inf")
            u.pre = self.nil
        s.color = "G"
        s.d = 0
        s.pre = self.nil
        q = Queue()
        q.create_queue(10)
        q.enqueue(s)
        while not q.is_empty:
            u = q.dequeue()
            for v in self.adj[u]:
                if v.color == "W":
                    v.color = "G"
                    v.d = u.d + 1
                    v.pre = u
                    Q.enqueue(v)
            u.color = "B"
            print(u, u.color)


class DFS:

    def __init__(self):
        self.time = 0
        self.vertices = None

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


a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")
f = Vertex("f")
g = Vertex("g")
h = Vertex("h")
connections = [(a, b), (b, c), (b, e), (b, f), (c, d), (c, g), (d, c), (d, h), (e, a), (e, f), (f, g), (g, f), (g, h), (h, h)]
g = Graph(connections, directed=True)
print(g.bfs(a))


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
