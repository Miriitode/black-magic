from functools import cache


# some DP solution
def sdsp(n, edges, t):
    assert 0 <= t < n

    adj = [[] for _ in range(n)]
    for i, j, c in edges:
        adj[i].append((j, c))

    # d(i) = min (c + d(j)) for all (j, c) in adj[i]
    # d(t) = 0

    @cache
    def d(i, k):
        # shortest path from i to t with at most k edges

        if i == t:
            return 0
        elif k == 0:
            return float('inf')
        else:
            return min((c + d(j, k-1) for j, c in adj[i]), default=float('inf'))


    return [d(i, n-1) for i in range(n)]


if __name__ == '__main__':
    print(sdsp(7, [
            (0, 1, 3), 
            (0, 3, 99),
            (0, 2, 2),
            (1, 2, 1),
            (2, 3, 5),
            (2, 5, 2),
            (5, 3, 2),
            (4, 3, 3),
        ], 3))
