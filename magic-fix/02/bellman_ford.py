# Bellman-Ford algorithm
def sssp(n, edges, s):

    d = [float('inf')]*n
    d[s] = 0

    for _ in range(n):
        did_something = False
        for i, j, c in edges:
            if d[j] > d[i] + c:
                d[j] = d[i] + c
                did_something = True

        if not did_something:
            return d

    return None


if __name__ == '__main__':
    print(sssp(7, [
            (0, 1, 3), 
            (0, 3, 99),
            (0, 2, 2),
            (1, 2, 1),
            (2, 3, 1),
            (2, 5, 2),
            (5, 3, -1000),
            (4, 3, 3),

            # add these to form a cycle
            # (1, 6, 500),
            # (6, 0, -600),
        ], 0))
