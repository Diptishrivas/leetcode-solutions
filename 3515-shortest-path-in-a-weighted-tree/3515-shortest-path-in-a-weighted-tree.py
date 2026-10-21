class Solution(object):
    def treeQueries(self, n, edges, queries):
   
        graph = [[] for _ in range(n + 1)]
        edge_weight = {}

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            edge_weight[(min(u, v), max(u, v))] = w

        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        parent = [0] * (n + 1)
        weight = [0] * (n + 1)
        timer = 0

        stack = [(1, 0, 0, 0)]

        while stack:
            u, p, w, state = stack.pop()

            if state == 0:
                timer += 1
                tin[u] = timer
                parent[u] = p
                weight[u] = w
                stack.append((u, p, w, 1))

                for v, ew in reversed(graph[u]):
                    if v != p:
                        stack.append((v, u, ew, 0))
            else:
                tout[u] = timer

        bit = [0] * (n + 2)

        def update(i, delta):
            while i <= n:
                bit[i] += delta
                i += i & (-i)

        def prefix_sum(i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & (-i)
            return result

        for u in range(2, n + 1):
            update(tin[u], weight[u])
            update(tout[u] + 1, -weight[u])

        ans = []

        for q in queries:
            if q[0] == 1:
                u, v, new_w = q[1], q[2], q[3]

                if parent[u] == v:
                    child = u
                else:
                    child = v

                delta = new_w - weight[child]
                weight[child] = new_w

                update(tin[child], delta)
                update(tout[child] + 1, -delta)

            else:
                x = q[1]
                ans.append(prefix_sum(tin[x]))

        return ans