from collections.abc import Sequence, Iterable

from utils import Edge


class UnionFind:
    def __init__(self, n):
        self.parent = [*range(n)]
        self.weight = [1]*n
        super().__init__()

    def __getitem__(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self[self.parent[i]]
            return self.parent[i]

    def unite(self, i, j):
        if (i := self[i]) == (j := self[j]):
            return False

        if self.weight[i] > self.weight[j]:
            i, j = j, i

        assert self.weight[i] <= self.weight[j]

        self.weight[j] += self.weight[i]
        self.parent[i] = j

        return True


def mst(n: int, edges: Sequence[Edge]) -> list[Edge]:
    tree = []
    comps = UnionFind(n)
    for edge in sorted(edges, key=lambda edge: edge.cost):
        if comps.unite(edge.i, edge.j):
            tree.append(edge)

    return tree


def mst_cost(n, edges):
    return sum(edge.cost for edge in mst(n, edges))


def main():
    print(mst_cost(5, [
        Edge(i=0, j=1, cost=4),
        Edge(i=0, j=2, cost=2),
        Edge(i=1, j=2, cost=4),
        Edge(i=1, j=3, cost=6),
        Edge(i=1, j=4, cost=6),
        Edge(i=3, j=4, cost=9),
        Edge(i=2, j=3, cost=8),
    ]))


if __name__ == '__main__':
    main()
