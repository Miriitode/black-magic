from itertools import count

import kruskal
import prim

from utils import Edge


def main():
    from random import Random

    rand = Random(11)

    def rand_cost():
        # return rand.randint(1, 10**9)
        return rand.randint(1, 100)

    def rand_edge(n):
        i = rand.randrange(n)
        j = rand.randrange(n)
        return Edge(i=i, j=j, cost=rand_cost())

    def rand_tree(n):
        labels = [*range(n)]
        rand.shuffle(labels)
        for i in range(1, n):
            j = rand.randrange(i)
            if rand.randrange(2):
                i, j = j, i
            yield Edge(i=labels[i], j=labels[j], cost=rand_cost())

    def rand_graph():
        n = rand.randint(1, rand.choice([5, 10, 20, 50, 100]))
        e = rand.randint(0, rand.choice([10, 2*n + 5, n**2 * 2 + 3]))
        edges = [rand_edge(n) for _ in range(e)]
        edges += rand_tree(n)

        rand.shuffle(edges)
        return n, edges

    for case in count(1):
        n, edges = rand_graph()

        # print(f'random graph #{case}:')
        # print(f'{n = }')
        # for edge in edges:
        #     print(edge)
        # print()

        ans_k = kruskal.mst_cost(n, edges)
        ans_p = prim.mst_cost(n, edges)

        print(f"Case {case}: {n=} e={len(edges)} {ans_k=} {ans_p=}")

        assert ans_k == ans_p, f"{n=}, {edges=}: {ans_k=}, {ans_p=}"


if __name__ == '__main__':
    main()
