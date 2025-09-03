from utils import Edge


def bridges_and_artic_points(n, edges):
    adj = [[] for _ in range(n)]
    for idx, edge in enumerate(edges):
        adj[edge.i].append((edge.j, idx))
        adj[edge.j].append((edge.i, idx))

    disc = [-1]*n  # disc[i] = discovery time of node i during DFS
    low = [-1]*n   # low[i] = earliest discovery time among nodes reachable from i's subtree using at most one back edge
    time = 0
    bridges = []
    artic_points = []

    def dfs(i, parent_idx, is_root):
        nonlocal time
        assert disc[i] == -1

        disc[i] = time; time += 1
        low[i] = disc[i]

        has_putolable_child = False
        children_count = 0
        for j, idx in adj[i]:
            if disc[j] == -1:
                # tree edge

                children_count += 1

                dfs(j, idx, False)

                low[i] = min(low[i], low[j])

                # check if bridge
                if low[j] > disc[i]:
                    bridges.append(edges[idx])

                # check if has identified a child na putolable from the rest
                if low[j] >= disc[i]:
                    has_putolable_child = True

            elif parent_idx != idx:
                # back edge

                low[i] = min(low[i], disc[j])

            # else:
            #     pass  # this is the parent edge... ignore

        if not is_root and has_putolable_child or is_root and children_count >= 2:
            artic_points.append(i)

    for s in range(n):
        if disc[s] == -1:
            # run a new DFS from this connected component
            dfs(s, -1, True)

    assert -1 not in disc

    return bridges, artic_points


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

    bridges, artic_points = bridges_and_artic_points(n, edges)

    print(*bridges)
    print(*artic_points)


if __name__ == '__main__':
    main()
