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
        self.val = i
        self.color = None
        self.d = None
        self.pre = None


class Graph:

    def __init__(self):
        nil = Vertex()
        self.vertices = []
        self.edges = []
        self.nil = nil

    def bfs(self, s):
        for u in vertices:
            u.color = "W"
            u.d = float("inf")
            u.pre = nil
        s.color = "G"
        s.d = 0
        s.pre = nil
        Q = Queue()
        Q.enqueue(s)
        while not Q.is_empty:
            u = Q.dequeue()
            for v in G.adj[u]:
                if v.color == "W":
                    v.color = "G"
                    v.d = u.d + 1
                    v.pre = u
                    Q.enqueue(v)
            u.color = "B"

    def dfs_visit(self, u):
        time += 1
        u.d = time
        u.color = "G"
        for v in G.adj[u]:
            if v.color == "W":
                v.pre = u
                dfs(G, v)
        u.color = "B"
        time += 1
        u.f = time

    def dfs(self):
        for u in G.V:
            u.color = "W"
            u.pre = nil
        time = 0
        for u in G.V:
            if u.color == "W":
                dfs_visit(G, u)
