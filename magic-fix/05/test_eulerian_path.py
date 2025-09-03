from itertools import count

from hierholzer import eulerian_path
from utils import CS33Random, Edge


def main():
    rand = CS33Random(33)

    for cas in count():
        n = rand.randint(1, rand.choice([3, 11, 21, 31]))
        e = rand.randint(0, rand.choice([3, 11, n + 5, 2*n + 5, 4*n + 5, n**2//2 + 11, n**2 + 5]))
        e += n - 1
        edges = rand.rand_connected_graph(n, e)

        degs = [0]*n
        for i, j in edges:
            degs[i] += 1
            degs[j] += 1

        bads = rand.shuffled(i for i in range(n) if degs[i] % 2)

        if rand.random() < 0.8:
            targ = rand.choice([0, 2])
            # make sure everything has even degree except 0 or 2
            assert len(bads) % 2 == 0
            while len(bads) > targ:
                i, j = (bads.pop() for _ in range(2))
                edges.append((i, j))

            assert len(bads) <= targ
        else:
            targ = None

        e = len(edges)

        edges = tuple(Edge(i, j, idx=idx) for idx, (i, j) in enumerate(rand.shuffled(edges)))

        eulpath = eulerian_path(n, edges)

        print(f"Case {cas}: {n=} {e=}")

        if eulpath is not None:
            assert len(eulpath) == len(edges)
            assert sorted(eulpath) == sorted(edges)

            def walk_from(start):
                curr = start
                for edge in eulpath:
                    if (curr := edge.other(curr)) is None:
                        return False
                return True

            start, *_ = [start for start in (eulpath[0].nodes() if eulpath else [0]) if walk_from(start)]


            def node_seq(start=0):
                curr = start
                yield start
                for edge in eulpath:
                    yield (curr := edge.other(curr))
                assert (curr == start) == (len(bads) == 0)

            print(*node_seq(start), sep=' -> ')

        assert (eulpath is not None) == (targ is not None or len(bads) <= 2)


if __name__ == '__main__':
    main()
