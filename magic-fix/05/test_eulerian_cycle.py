from itertools import count

from hierholzer import eulerian_cycle
from utils import CS33Random, Edge


def main():
    rand = CS33Random(33)

    for cas in count():
        n = rand.randint(1, rand.choice([3, 11, 21, 31]))
        e = rand.randint(0, rand.choice([3, 11, n + 5, 2*n + 5, 4*n + 5, n**2//2 + 11, n**2 + 5]))
        e += n - 1
        edges = rand.rand_connected_graph(n, e)

        # make sure everything has even degree
        degs = [0]*n
        for i, j in edges:
            degs[i] += 1
            degs[j] += 1

        bads = rand.shuffled(i for i in range(n) if degs[i] % 2)
        assert len(bads) % 2 == 0
        while bads:
            i, j = (bads.pop() for _ in range(2))
            edges.append((i, j))

        e = len(edges)

        edges = tuple(Edge(i, j, idx=idx) for idx, (i, j) in enumerate(rand.shuffled(edges)))

        eulcyc = [*eulerian_cycle(n, edges)]

        print(f"Case {cas}: {n=} {e=}")

        assert len(eulcyc) == len(edges)
        assert sorted(eulcyc) == sorted(edges)

        def node_seq(start=0):
            curr = start
            yield start
            for edge in eulcyc:
                yield (curr := edge.other(curr))
            assert curr == start

        print(*node_seq(), sep=' -> ')


if __name__ == '__main__':
    main()
