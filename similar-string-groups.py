class UnionFind:
    def __init__(self, n):
        self.rep = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}
    
    def find(self, node):
        if self.rep[node] == node:
            return self.rep[node]
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]

    def union(self,x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep != yrep:
            if self.size[xrep] > self.size[yrep]:
                xrep, yrep = yrep, xrep
            self.size[yrep] += self.size[xrep]
            self.rep[xrep] = yrep 

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        unionfind = UnionFind(N)
        for i in range(N):
            for j in range(i + 1, N):
                diff = 0
                for k in range(len(strs[i])):
                    diff += (strs[i][k] != strs[j][k])
                    if diff > 2:
                        break
                if diff < 3:
                    unionfind.union(i, j)
        visited = set()
        for i in range(N):
            visited.add(unionfind.find(i))
        return len(visited)