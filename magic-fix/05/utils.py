from dataclasses import dataclass
from random import Random

@dataclass(frozen=True, order=True)
class Edge:
    i: int
    j: int
    idx: int

    def other(self, i):
        if i == self.i:
            return self.j
        if i == self.j:
            return self.i
        return None

    def nodes(self):
        yield self.i
        yield self.j


class CS33Random(Random):
    def shuffled(self, seq):
        seq = list(seq)
        self.shuffle(seq)
        return seq

    def rand_graph(self, n, e):
        edges = []
        while len(edges) < e:
            i = self.randrange(n)
            j = self.randrange(n)
            edges.append((i, j))
        assert len(edges) == e
        return edges

    def rand_tree(self, n):
        labels = self.shuffled(range(n))
        edges = []
        for i in range(1, n):
            j = self.randrange(i)
            edges.append((labels[i], labels[j]))

        return self.shuffled(tuple(self.shuffled(edge)) for edge in edges)

    def rand_connected_graph(self, n, e):
        assert e >= n - 1
        edges = self.shuffled((
            *self.rand_graph(n, e - (n - 1)),
            *self.rand_tree(n),
        ))
        assert len(edges) == e

        return self.shuffled(tuple(self.shuffled(edge)) for edge in edges)
