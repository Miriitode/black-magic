from collections.abc import Sequence
from collections import deque


def find_shortest_paths(n: int, edges: Sequence[tuple[int, int]], s: int) -> list[int]:
    adj: list[list[int]] = [[] for _ in range(n)]

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    to_visit = deque([s])
    distances: list[int] = [float('inf')] * n
    distances[s] = 0
    visited: set[int] = {s}
    while to_visit:
        i = to_visit.popleft()
        assert i in visited
        for j in adj[i]:
            if j not in visited:
                to_visit.append(j)
                visited.add(j)
                distances[j] = distances[i] + 1

    return distances


# def solve_something(a, b, c):
#     find_shortest_paths(???)


if __name__ == '__main__':
    print(find_shortest_paths(7, [
        (2, 3),
        (2, 6),
        (3, 6),
        (1, 4),
        (5, 4),
    ], 1))

    print(find_shortest_paths(7, [
        (0, 1),
        (0, 4),
        (1, 4),
        (1, 2),
        (1, 3),
        (4, 3),
        (2, 3),
        (2, 5),
        (3, 5),
        (3, 6),
        (5, 6),
    ], 0))
