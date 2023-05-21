class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        rep = {i: i for i in range(N)}
        size = {i: 1 for i in range(N)}
        cost = 0
        
        def find(node):
            if rep[node] == node:
                return rep[node]
            rep[node] = find(rep[node])
            return rep[node]

        def union(x, y, val):
            nonlocal cost
            xrep = find(x)
            yrep = find(y)
            if xrep != yrep:
                if size[xrep] > size[yrep]:
                    xrep, yrep = yrep, xrep
                size[yrep] += size[xrep]
                rep[xrep] = yrep
                cost += val

        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append((i, j, abs(x1 - x2) + abs(y1 - y2)))

        edges.sort(key=lambda x: x[2])
        for edge in edges:
            x, y, val = edge
            union(x, y, val)
        return cost