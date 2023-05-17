class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        rep = {i:i for i in range(n)}
        size = {i:1 for i in range(n)}

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
        
        for x, y in edges:
            union(x, y)
        return find(source) == find(destination)
"""


            xrep = find(x)
            yrep = find(y)
            if rank[xrep] > rank[yrep]:
                xrep, yrep = yrep, xrep
            if rank[xrep] == rank[yrep]:
                rank[yrep] += 1
            rep[xrep] = yrep

"""