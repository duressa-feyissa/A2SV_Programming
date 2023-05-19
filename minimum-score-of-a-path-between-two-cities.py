class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjacent = defaultdict(list)
        rep = {i: i for i in range(1, n+1)}
        size = {i: 1 for i in range(1, n+ 1)}
        Min = {i: 10**5  for i in range(1,  n+ 1)}

        def find(node):
            if rep[node] == node:
               return rep[node]
            rep[node] = find(rep[node])
            return rep[node]

        def union(x, y, z):
            xrep = find(x)
            yrep = find(y)
            minimum = min([Min[xrep], Min[yrep], z])
            
            if size[xrep] > size[yrep]:
                xrep, yrep = yrep, xrep
            size[yrep] += size[xrep]
            rep[xrep] = yrep
            Min[yrep] = minimum

        for x,y, z in roads:
            union(x, y, z)
        
        x = find(1)
        y = find(n)
        return min(Min[x], Min[y])