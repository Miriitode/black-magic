from heapq import heappush, heappop


# Prim's algorithm
def mst_cost(n, edges):
    adj = [[] for _ in range(n)]
    for i, j, c in edges:
        adj[i].append((j, c))
        adj[j].append((i, c))

    s = 0  # arbitrary node as starting point
    pq = [(0, s)]

    vis = [False]*n

    total = 0
    while pq:
        d, i = heappop(pq)

        if vis[i]:
            continue

        vis[i] = True
        total += d

        for j, c in adj[i]:
            heappush(pq, (c, j))  # 'c' is the cost if we attach j using this edge

    return total


# Dijkstra's algorithm
def sssp(n, edges, s):
    adj = [[] for _ in range(n)]
    for i, j, c in edges:
        adj[i].append((j, c))
        # directed, so we don't include j -> i

    pq = [(0, s)]

    vis = [False]*n
    dist = [float('inf')]*n

    while pq:
        d, i = heappop(pq)

        if vis[i]:
            continue

        vis[i] = True
        dist[i] = d

        for j, c in adj[i]:
            heappush(pq, (d + c, j))  # 'd + c' is the distance to j using this edge

    return dist


if __name__ == '__main__':
    print(sssp(7, [
            (0, 1, 3), 
            (0, 3, 99),
            (0, 2, 2),
            (1, 2, 1),
            (2, 3, 5),
            (2, 5, 2),
            (5, 3, 2),
            (4, 3, 3),
        ], 0))

    print(sssp(7, [
            (0, 1, 3), 
            (0, 3, 99),
            (0, 2, 2),
            (1, 2, 1),
            (2, 3, 1),
            (2, 5, 2),
            (5, 3, -1000),
            (4, 3, 3),
        ], 0))
