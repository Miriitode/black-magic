from collections.abc import Sequence
from collections import deque


def find_connected_components(n: int, edges: Sequence[tuple[int, int]]) -> list[list[int]]:
    visited: set[int] = set()

    adj: list[list[int]] = [[] for _ in range(n)]

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    # def get_all_nodes_reachable_from(s: int):
    #     return list(_get_all_nodes_reachable_from(s))

    # def _get_all_nodes_reachable_from(s: int):
    #     if s not in visited:
    #         yield s
    #         visited.add(s)
    #         for t in adj[s]:
    #             yield from _get_all_nodes_reachable_from(t)

    def get_all_nodes_reachable_from(s: int):
        # to_visit = [s]
        to_visit = deque([s])
        reachable = []
        while to_visit:
            # i = to_visit.pop()
            i = to_visit.popleft()
            if i not in visited:
                reachable.append(i)
                visited.add(i)
                to_visit += adj[i]

        return reachable

    answer: list[list[int]] = []
    for i in range(n):
        if i not in visited:
            answer.append(get_all_nodes_reachable_from(i))

    return answer

if __name__ == '__main__':
    print(find_connected_components(7, [
        (2, 3),
        (2, 6),
        (3, 6),
        (1, 4),
        (5, 4),
    ]))

    print(find_connected_components(5, [
        (0, 1),
        (0, 4),
        (1, 4),
        (1, 2),
        (1, 3),
        (4, 3),
    ]))
