from collections.abc import Sequence
from collections import deque


def find_connected_components(n: int, edges: Sequence[tuple[int, int]]) -> list[list[int]]:
    adj: list[list[int]] = [[] for _ in range(n)]

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    visited: list[bool] = [False]*n

    # def get_all_nodes_reachable_from(s: int):
    #     return list(_get_all_nodes_reachable_from(s))

    # def _get_all_nodes_reachable_from(s: int):
    #     if not visited[s]:
    #         yield s
    #         visited[s] = True
    #         for t in adj[s]:
    #             yield from _get_all_nodes_reachable_from(t)

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


def make_graph(grid: str):
    lines = [row.split() for row in grid.splitlines()]

    r = len(lines)
    [c] = {*map(len, lines)}
    nodes = [
            (i, j)
            for i in range(r)
            for j in range(c)
            if lines[i][j] == '.'
        ]
    node_index = {node: i for i, node in enumerate(nodes)}

    def neighbors(i, j):
        for di, dj in (1, 0), (0, 1):
            ni = i + di
            nj = j + dj
            if 0 <= ni < r and 0 <= nj < c and lines[ni][nj] == '.':
                yield ni, nj

    edges = []
    for i, j in nodes:
        for ni, nj in neighbors(i, j):
            edges.append((node_index[i, j], node_index[ni, nj]))

    return len(nodes), edges


def count_rooms(grid: str) -> int:
    return len(find_connected_components(*make_graph(grid)))


if __name__ == '__main__':
    grid = """\
. . . # .
. . . # .
. . # . .
. . . # .
. # # . #
# . . . .
. . . . .
"""
    print(count_rooms(grid))
