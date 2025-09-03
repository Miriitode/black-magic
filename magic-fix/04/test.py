from itertools import count

import cut_brute_force
import cut_dfs

from utils import Edge


def normalize(bridges_and_artic_points):
    # normalize output so they can be compared
    def norm_bridges_and_artic_points(n, edges):
        bridges, artic_points = bridges_and_artic_points(n, edges)
        return sorted(bridges), sorted(artic_points)

    return norm_bridges_and_artic_points


def main():
    from random import Random

    rand = Random(33)

    def rand_edge(n):
        i = rand.randrange(n)
        j = rand.randrange(n)
        return Edge(i=i, j=j)

    def rand_graph():
        n = rand.randint(1, rand.choice([5, 10, 20]))
        e = rand.randint(0, rand.choice([10, 2*n + 5, n**2 * 2 + 3]))
        edges = [rand_edge(n) for _ in range(e)]

        rand.shuffle(edges)
        return n, edges

    sols = (
        normalize(cut_brute_force.bridges_and_artic_points),
        normalize(cut_dfs.bridges_and_artic_points),
    )

    for case in count(1):
        n, edges = rand_graph()

        # print(f'random graph #{case}:')
        # print(f'{n = }')
        # for edge in edges:
        #     print(edge)
        # print()

        answers = [sol(n, edges) for sol in sols]

        answer = answers[0]

        print(f"Case {case}: {n=} e={len(edges)}")
        # bridges, artic_points = answer
        # print(f"{bridges = }")
        # print(f"{artic_points = }")

        assert all(ans == answer for ans in answers), f"{n=}, {edges=}: {answers=}"


if __name__ == '__main__':
    main()
