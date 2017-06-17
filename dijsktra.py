class DijkVertex(Vertex):

    def decrease_key(self, q):
        prio = self.priority
        ndx = prio.ndx
