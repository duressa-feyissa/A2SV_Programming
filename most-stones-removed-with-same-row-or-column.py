class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        rep = {i: i for i in range(1, N+1)}
        size = {i: 1 for i in range(1, N+ 1)}
        Map = {tuple(stones[i - 1]): i for i in range(1, N + 1)}

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
        
        for i in range(N):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    xrep = find(Map[tuple(stones[i])])
                    yrep = find(Map[tuple(stones[j])])
                    if xrep != yrep:
                        union(Map[tuple(stones[i])], (Map[tuple(stones[j])]))
        total = 0
        visited = set()
        for i in range(N):
            parent = find(Map[tuple(stones[i])])
            if parent not in visited:
                total += (size[parent] - 1)
            visited.add(parent)
        return total