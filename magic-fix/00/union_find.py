from collections.abc import Sequence
from collections import deque
from itertools import combinations


def find_connected_components(n: int, edges: Sequence[tuple[int, int]]) -> list[list[int]]:
    adj: list[list[int]] = [[] for i in range(n)]

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    # def get_all_nodes_reachable_from(s: int):
    #     return list(_get_all_nodes_reachable_from(s))

    # def _get_all_nodes_reachable_from(s: int):
    #     if not visited[s]:
    #         yield s
    #         visited[s] = True
    #         for t in adj[s]:
    #             yield from _get_all_nodes_reachable_from(t)

    visited: list[bool] = [False]*n

    def get_all_nodes_reachable_from(s: int):
        # to_visit = [s]
        to_visit = deque([s])
        reachable = []
        while to_visit:
            # i = to_visit.pop()
            i = to_visit.popleft()
            if not visited[i]:
                reachable.append(i)
                visited[i] = True
                to_visit += adj[i]

        return reachable

    answer: list[list[int]] = []
    for i in range(n):
        if not visited[i]:
            answer.append(get_all_nodes_reachable_from(i))

    return answer


class DisjointSets:
    def __init__(self, n: int):
        self.n = n
        self.parent = [None]*n
        self.size = [1]*n
        super().__init__()

    def root(self, i: int):
        if self.parent[i] is None:
            return i
        else:
            # path compression
            self.parent[i] = self.root(self.parent[i])
            return self.parent[i]

    def in_same_set(self, i: int, j: int) -> bool:
        return self.root(i) == self.root(j)

    def merge(self, i: int, j: int) -> None:
        if not self.in_same_set(i, j):
            i = self.root(i)
            j = self.root(j)

            # union by weight
            if self.size[j] < self.size[i]:
                i, j = j, i

            assert self.size[j] >= self.size[i]

            self.size[j] += self.size[i]
            self.parent[i] = j


class Graph:
    def __init__(self, n: int, edges: Sequence[tuple[int, int]]):
        self.n = n
        self.comps: DisjointSets = DisjointSets(n)
        for x, y in edges:
            self.comps.merge(x, y)
        super().__init__()

    def is_connected(self, i: int, j: int) -> bool:
        return self.comps.in_same_set(i, j)

    def add_edge(self, i: int, j: int):
        self.comps.merge(i, j)


if __name__ == '__main__':
    graph = Graph(7, [
        (2, 3),
        (2, 6),
        (3, 6),
        (1, 4),
        (5, 4),
    ])

    def print_connected_pairs():
        for i, j in combinations(range(graph.n), 2):
            if graph.is_connected(i, j):
                print(f'{i} and {j} are connected')

    print_connected_pairs()
    graph.add_edge(6, 4)
    print('added')
    print_connected_pairs()
