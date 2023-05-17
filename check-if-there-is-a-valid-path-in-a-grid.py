class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = [{2, 5, 6}, {2, 3, 4}]   
        left = [{1, 3, 5}, {1, 4, 6}] 
        right = [{1, 4, 6}, {1, 3, 5}] 
        down = [{2, 3, 4}, {2, 5, 6}] 
        M = len(grid)
        N = len(grid[0])
        k = 0
        unique = {}

        def inbound(r, c):
            return 0 <= r < M and 0 <= c < N
        unique = {}
        k = 1
        path = []
        for i in range(M):
            for j in range(N):
                unique[(i, j)] = k
                k += 1

        for i in range(M):
            for j in range(N):
                if inbound(i, j - 1) and grid[i][j] in left[0] and grid[i][j - 1] in left[1]:
                    path.append((unique[(i, j)], unique[(i, j - 1)]))
                if inbound(i, j + 1) and grid[i][j] in right[0] and grid[i][j + 1] in right[1]:
                    path.append((unique[(i, j)], unique[(i, j + 1)]))
                if inbound(i - 1, j) and grid[i][j] in up[0] and grid[i - 1][j] in up[1]:
                    path.append((unique[(i, j)], unique[(i - 1, j)]))
                if  inbound(i + 1, j) and grid[i][j] in down[0] and grid[i + 1][j] in down[1]:
                    path.append((unique[(i, j)], unique[(i + 1, j)]))

        rep = {i:i for i in range(1, M * N + 1)}
        size = {i:1 for i in range(1, M * N + 1)}

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
        
        for x, y in path:
            union(x, y)
        
        return find(1) == find(M*N)