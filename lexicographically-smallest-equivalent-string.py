class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {i: i for i in range(26)}
        size = {i: 1 for i in range(26)}
        Map = {chr(i + 97): i for i in range(26)}
         
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
        N = len(s1)
        groups = defaultdict(list)
        
        for i in range(N):
            union(Map[s1[i]], Map[s2[i]])
        text = set(list(s1) + list(s2))
        
        for c in text:
            groups[find(Map[c])].append(c)
        for i in range(26):
            groups[i].sort()
    
        answer = ""
        for c in baseStr:
            if c in text:
                char = rep[Map[c]]
                answer += groups[char][0]
            else:
                answer += c
        return answer