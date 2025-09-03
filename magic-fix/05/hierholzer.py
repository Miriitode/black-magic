from collections import deque

from utils import Edge


def eulerian_cycle(n, edges, start=0):
    assert 0 <= start < n

    used_edge = [False]*len(edges)
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge.i].append((edge.j, edge))
        adj[edge.j].append((edge.i, edge))

    assert all(len(adj[i]) % 2 == 0 for i in range(n))

    def consume(i):
        # keep on walking until no more edges
        # must return to i
        curr = i
        while adj[curr]:
            bago, edge = adj[curr].pop()
            assert 0 <= edge.idx < len(edges)
            if not used_edge[edge.idx]:
                used_edge[edge.idx] = True
                curr = bago
                yield curr, edge

        assert curr == i

    considering = deque([(start, None)])
    while considering:
        i, edge = considering.popleft()
        if edge is not None:
            yield edge

        new_edges = deque(consume(i))
        while new_edges:
            considering.appendleft(new_edges.pop())

    assert all(used_edge)


def eulerian_path(n, edges):
    degs = [0]*n
    for edge in edges:
        degs[edge.i] += 1
        degs[edge.j] += 1

    bads = [i for i in range(n) if degs[i] % 2]
    assert len(bads) % 2 == 0

    match bads:
        case []:
            return [*eulerian_cycle(n, edges)]
        case [a, b]:
            dummy = Edge(i=a, j=b, idx=len(edges))
            cyc = [*eulerian_cycle(n, [*edges, dummy])]
            idx = cyc.index(dummy)
            return [*cyc[idx+1:], *cyc[:idx]]
        case _:
            return None
