from itertools import count

import dijkstra
import dp
import dp2
import floyd
import bellman_ford

from utils import Edge


def apsp_from_sdsp(sdsp):
    def apsp(n, edges):
        d = [sdsp(n, edges, t) for t in range(n)]
        return [[d[t][s] for t in range(n)] for s in range(n)]
    return apsp


def apsp_from_sssp(sssp):
    def apsp(n, edges):
        return [sssp(n, edges, s) for s in range(n)]
    return apsp


def main():
    from random import Random

    rand = Random(11)

    def rand_cost():
        # return rand.randint(0, 10**9)
        return rand.randint(0, 100)

    def rand_edge(n):
        i = rand.randrange(n)
        j = rand.randrange(n)
        return Edge(i=i, j=j, cost=rand_cost())

    def rand_graph():
        n = rand.randint(1, rand.choice([5, 10, 20]))
        e = rand.randint(0, rand.choice([10, 2*n + 5, n**2 * 2 + 3]))
        edges = [rand_edge(n) for _ in range(e)]

        rand.shuffle(edges)
        return n, edges

    apsp_sols = (
        apsp_from_sdsp(dp.sdsp),
        apsp_from_sssp(dijkstra.sssp),
        dp2.apsp,
        floyd.apsp,
        apsp_from_sssp(bellman_ford.sssp),
    )

    for case in count(1):
        n, edges = rand_graph()

        # print(f'random graph #{case}:')
        # print(f'{n = }')
        # for edge in edges:
        #     print(edge)
        # print()

        answers = [apsp(n, edges) for apsp in apsp_sols]

        answer = answers[0]

        print(f"Case {case}: {n=} e={len(edges)}")
        # for row in answer:
        #     print(*row)

        assert all(ans == answer for ans in answers), f"{n=}, {edges=}: {answers=}"


if __name__ == '__main__':
    main()
