from utils import Edge


def count_cc(nodes, edges):
    adj = {node: [] for node in nodes}
    for edge in edges:
        adj[edge.i].append(edge.j)
        adj[edge.j].append(edge.i)
    count = 0
    vis = set()
    for s in nodes:
        if s not in vis:
            count += 1
            vis.add(s)
            stak = [s]
            while stak:
                i = stak.pop()
                for j in adj[i]:
                    if j not in vis:
                        vis.add(j)
                        stak.append(j)

    return count


def bridges(n, edges):
    cc = count_cc(range(n), edges)
    for idx, edge in enumerate(edges):
        rem_edges = [*edges[:idx], *edges[idx+1:]]
        if count_cc(range(n), rem_edges) > cc:
            yield edge


def artic_points(n, edges):
    cc = count_cc(range(n), edges)
    for i in range(n):
        rem_nodes = [j for j in range(n) if j != i]
        rem_edges = [edge for edge in edges if i not in (edge.i, edge.j)]
        if count_cc(rem_nodes, rem_edges) > cc:
            yield i


def bridges_and_artic_points(n, edges):
    return bridges(n, edges), artic_points(n, edges)


def main():
    n = 8
    edges = (
        Edge(0, 2),
        Edge(5, 2),
        Edge(5, 4),
        Edge(0, 4),
        Edge(2, 3),
        Edge(3, 1),
        Edge(1, 7),
        Edge(7, 3),
        Edge(7, 6),
    )

    print(*bridges(n, edges))
    print(*artic_points(n, edges))


if __name__ == '__main__':
    main()
