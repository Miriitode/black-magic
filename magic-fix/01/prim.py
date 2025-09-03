from collections.abc import Sequence, Iterable
# from heapq import heappush, heappop

from utils import Edge


def heappush(heap, val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        if heap[p := i - 1 >> 1] > heap[i]:
            heap[p], heap[i] = heap[i], heap[p]
            i = p
        else:
            break


def heappop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    res = heap.pop()
    i = 0
    while (c := 2*i + 1) < len(heap):
        if c + 1 < len(heap) and heap[c] > heap[c + 1]:
            c += 1
        if heap[i] > heap[c]:
            heap[i], heap[c] = heap[c], heap[i]
            i = c
        else:
            break

    return res


def mst(n: int, edges: Sequence[Edge]) -> list[Edge]:

    adj = [[] for _ in range(n)]

    for edge in edges:
        adj[edge.i].append((edge.j, edge))
        adj[edge.j].append((edge.i, edge))


    # start from some node (say node 0)
    included = {0}

    def can_add(edge: Edge) -> bool:
        if edge.i in included and edge.j not in included:
            return True
        if edge.j in included and edge.i not in included:
            return True
        return False

    to_add = []

    for j, edge in adj[0]:
        heappush(to_add, edge)

    tree = []
    while len(tree) < n - 1:
        edge = heappop(to_add)

        if edge.i in included and edge.j in included:
            continue

        tree.append(edge)
        included.add(edge.i)
        included.add(edge.j)

        for i in edge.i, edge.j:
            for j, edge in adj[i]:
                heappush(to_add, edge)

    return tree


def mst_cost(n, edges):
    return sum(edge.cost for edge in mst(n, edges))


def main():
    print(mst_cost(5, [
        Edge(i=0, j=1, cost=4),
        Edge(i=0, j=2, cost=2),
        Edge(i=1, j=2, cost=4),
        Edge(i=1, j=3, cost=6),
        Edge(i=1, j=4, cost=6),
        Edge(i=3, j=4, cost=9),
        Edge(i=2, j=3, cost=8),
    ]))


if __name__ == '__main__':
    main()
