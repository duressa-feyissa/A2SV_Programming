class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        rep = {i:i for i in range(1, N + 1)}
        size = {i:1 for i in range(1,N + 1)}

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
        
        answer = [-1, -1]
        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
                answer[0] = x
                answer[1] = y
        return answer