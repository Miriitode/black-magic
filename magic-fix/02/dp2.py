from functools import cache

"""
k, i, j are nodes

s(k, i, j) := shortest path from i to j
assuming the only allowed intermediate nodes are
0, 1, ..., k

s(n-1, i, j) = shortest path from i to j

s(-1, i, j) = easy to compute

s(k, i, j) = 

- if doesn't pass through k. s(k-1, i, j).
- if it passes through k.
    - 1st leg: s(k-1, i, k)
    - 2nd leg: s(k-1, k, j)
    - total: s(k-1, i, k) + s(k-1, k, j)

s(k, i, j) = min(s(k-1, i, j), s(k-1, i, k) + s(k-1, k, j))
"""

# not-quite Floyd's algorithm
def apsp(n, edges):

    adjmat = [[float('inf')]*n for _ in range(n)]

    for i in range(n):
        adjmat[i][i] = 0

    for i, j, c in edges:
        adjmat[i][j] = min(adjmat[i][j], c)

    @cache
    def s(k, i, j):
        # shortest path from i to j
        # assuming the only allowed intermediate nodes are
        # 0, 1, ..., k-1

        if k == 0:
            # easy to compute
            return adjmat[i][j]
        else:
            return min(s(k-1, i, j), s(k-1, i, k-1) + s(k-1, k-1, j))

    return [
        [s(n, i, j) for j in range(n)]
        for i in range(n)
    ]


if __name__ == '__main__':
    for row in apsp(7, [
                (0, 1, 3), 
                (0, 3, 99),
                (0, 2, 2),
                (1, 2, 1),
                (2, 3, 5),
                (2, 5, 2),
                (5, 3, 2),
                (4, 3, 3),
            ]):
        print(' '.join(f"{v:>5}" for v in row))

