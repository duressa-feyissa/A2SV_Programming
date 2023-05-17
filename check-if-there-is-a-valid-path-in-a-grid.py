class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = [{2, 5, 6}, {2, 3, 4}]
        left = [{1, 3, 5}, {1, 4, 6}]
        right = [{1, 4, 6}, {1, 3, 5}]
        down = [{2, 3, 4}, {2, 5, 6}]
        M = len(grid)
        N = len(grid[0])
        k = 0

        def inbound(r, c):
            return 0 <= r < M and 0 <= c < N

        rep = {i: i for i in range(M * N)}
        size = {i: 1 for i in range(M * N)}

        def find(node):
            if rep[node] == node:
               return rep[node]
            rep[node] = find(rep[node])
            return rep[node]

        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            if size[xrep] > size[yrep]:
                xrep, yrep = yrep, xrep
            size[yrep] += size[xrep]
            rep[xrep] = yrep

        for i in range(M):
            for j in range(N):
                if inbound(i, j - 1) and grid[i][j] in left[0] and grid[i][j - 1] in left[1]:
                    union(i * N + j, i * N + j - 1)
                if inbound(i, j + 1) and grid[i][j] in right[0] and grid[i][j + 1] in right[1]:
                    union(i * N + j, i * N + j + 1)
                if inbound(i - 1, j) and grid[i][j] in up[0] and grid[i - 1][j] in up[1]:
                    union(i * N + j, (i - 1) * N + j)
                if inbound(i + 1, j) and grid[i][j] in down[0] and grid[i + 1][j] in down[1]:
                    union(i * N + j, (i + 1) * N + j)

        return find(0) == find(M * N - 1)