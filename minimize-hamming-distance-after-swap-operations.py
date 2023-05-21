from collections import Counter, defaultdict
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)
        rep = {i: i for i in range(N)}
        size = {i: 1 for i in range(N)}
        
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
        
        for x, y in allowedSwaps:
            repx = find(x)
            repy = find(y)
            if repx != repy:
                union(x, y)

        groups = defaultdict(list)
        for i in range(N):
            parent = find(i)
            groups[parent].append(i)
        
        count = 0
        visited = set()
        
        def dfs(node):
            nonlocal count
            if node in visited:
                return
            visited.add(node)
            New = Counter(map(lambda x: source[x], groups[node]))
            check = Counter(map(lambda x: target[x], groups[node]))
            count += sum((New - check).values())
            
            for child in groups[node]:
                dfs(child)
        
        for i in range(N):
            if i not in visited:
                dfs(i)
        
        return count