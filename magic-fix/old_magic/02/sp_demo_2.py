import math

from functools import cache
from heapq import heappush, heappop


G_w = {  # weighted graph with cycles
    0: [(3, 1), (7, 3), (8, 4)],
    1: [(3, 0), (1, 2), (4, 3)],
    2: [(1, 1), (2, 3)],
    3: [(7, 0), (4, 1), (2, 2), (3, 4)],
    4: [(8, 0), (3, 3)]
}

G_w_negcycle = {  # weighted graph with negative weight cycle
    0: [(5, 1), (2, 4)],
    1: [(6, 2)],
    2: [(-3, 1), (8, 3)],
    3: [],
    4: [(3, 5)],
    5: [(-6, 4), (7, 3)]
}

# (cost, node)
G1 = {  # DAG
    0: [(2, 1), (1, 7)],
    1: [(1, 2)],
    2: [(1, 3)],
    3: [(1, 4)],
    4: [(1, 5)],
    5: [(1, 6)],
    6: [],
    7: [(7, 6)]
}


def reverse_adj(n, adj):
    radj = {i: [] for i in range(n)}
    for i in range(n):
        for c, j in adj[i]:
            radj[j].append((c, i))
    return radj


G1_rev = reverse_adj(8, G1)


def sdsp_looping(adj, dest):  # single destination shortest path
    # only works on DAGs
    n = len(adj)
    @cache  # memoized
    def dist(src):  # shortest path cost from src to dest
        if src == dest:
            return 0
        else:
            return min((cost + dist(j) for (cost, j) in adj[src]), default=math.inf)

    return [dist(s) for s in range(n)]


def sdsp(adj, dest):  # single destination shortest path
    n = len(adj)
    @cache  # memoized
    def dist(src, steps):
        if src == dest:
            return 0
        elif steps == 0:
            return math.inf
        else:
            return min((cost + dist(j, steps - 1) for (cost, j) in adj[src]), default=math.inf)

    return [dist(s, n - 1) for s in range(n)]


def adjm_from_adjlist(adjlist):
    n = len(adjlist)
    A = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]
    for i in adjlist:
        for c, j in adjlist[i]:
            A[i][j] = c
    return A


def floyd(adj_m, n): # all pairs shortest paths with predecessor
    # O(n^2) space
    pred = [[None] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj_m[i][j] > adj_m[i][k] + adj_m[k][j]:
                    adj_m[i][j] = adj_m[i][k] + adj_m[k][j]
                    pred[i][j] = k
    return adj_m, pred


def dijkstra_slow(adj, S):  # (c, i)
    vis = set()
    dists = {i: math.inf for i in range(len(adj))}
    dists[S] = 0
    pred = {S: None}
    candidates = [(0, S)]
    while candidates:
        c, i = min(candidates)
        candidates.remove((c, i))  # removes first instance
        vis.add(i)
        for (c_neigh, i_neigh) in adj[i]:
            if i_neigh in vis:
                continue
            if dists[i] + c_neigh < dists[i_neigh]:
                dists[i_neigh] = dists[i] + c_neigh
                pred[i_neigh] = i
                candidates.append((c_neigh, i_neigh))
    return (dists, pred)


def dijkstra(adj, S):  # proof by induction
    # path costs to visited nodes so far are shortest path costs
    vis = set()
    dists = {i: math.inf for i in range(len(adj))}
    dists[S] = 0
    pred = {S: None}
    candidates = [(0, S)]
    while candidates:
        c, i = heappop(candidates)
        vis.add(i)
        for (c_neigh, i_neigh) in adj[i]:
            if i_neigh in vis:
                continue
            if dists[i] + c_neigh < dists[i_neigh]:
                dists[i_neigh] = dists[i] + c_neigh
                pred[i_neigh] = i
                heappush(candidates, (c_neigh, i_neigh))
    return (dists, pred)



def bellman_ford(adj, S):
    # edges = edgelist_from_adj(adj)
    vis = {i: math.inf for i in range(len(adj))}
    vis[S] = 0
    pred = {S: None}
    for _ in range(len(vis) - 1):
        for i in adj:
            for c, j in adj[i]:
                if vis[j] > vis[i] + c:
                    vis[j] = vis[i] + c
                    pred[j] = i

    for i in adj:  # negative weight cycle detection
        for c, j in adj[i]:
            if vis[j] > vis[i] + c:
                return (False, None, None)

    return (True, vis, pred)




costs = sdsp_looping(G1, 6)  # shortest path costs going to node 6
print(costs)

# costs = sdsp_looping(G_w, 4)  # should produce RecursionError
# print(costs)

costs = sdsp(G_w, 4)  # now works on graphs with cycles
print(costs)

dists, pred = dijkstra_slow(G_w, 0)
print(dists)
print(pred)
print('Reconstructing path from 0 to 3')
d = 3
path = []
while d is not None:
    path.append(str(d))
    d = pred[d]
print('->'.join(path[::-1]))

dists, pred = dijkstra(G_w, 0)
print(dists)
print(pred)
print('Reconstructing path from 0 to 3')
d = 3
path = []
while d is not None:
    path.append(str(d))
    d = pred[d]
print('->'.join(path[::-1]))


# dists, pred = dijkstra(G_w_negcycle, 0)  # should loop forever

no_neg_cycles, dists, pred = bellman_ford(G_w, 0)  # graph with no negative weight cycles
print(f'No negative cycles? {'Yes' if no_neg_cycles else 'No'}')
print(dists)
print(pred)

no_neg_cycles, dists, pred = bellman_ford(G_w_negcycle, 0)  # graph with negative weight cycle
print(f'No negative cycles? {'Yes' if no_neg_cycles else 'No'}')
print(dists)
print(pred)







