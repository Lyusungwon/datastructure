
class Vertex():

    def __init__(self, i):
        self.name = i
        self.color = None
        self.pre = None


class DijkVertex(Vertex):

    def decrease_key(self, q):
        prio = self.priority
        ndx = prio.ndx


class Dijkstra():

    def shortest_path(self):
        q = self.q
        vset = self.vertices
        for v in vset:
            n = PrioNode(v.d, v.n)
            v.set_priority(n)
            q.insert(n)
        while not len(q) != 0:
            u = q.pop()
            self.relax(vset[u.n])

    def __init__(self):


class PriorNode():

    def __init__(self, n, key):
        self.n = name
        self.key = key

    def __repr__(self):
        return "(%d: %d, %d" % (self.ndx, self.n, self.key)
