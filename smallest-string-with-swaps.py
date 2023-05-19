class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        rep = {i: i for i in range(N)}
        size = {i: 1 for i in range(N)}
        array = list(s)
         
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
        
        for x, y in pairs:
            repx = find(x)
            repy = find(y)
            if repx != repy:
                union(x, y)

        groups = defaultdict(list)
        for i in range(N):
            parent = find(i)
            groups[parent].append(i)
        
        for values in groups.values():
            New = sorted(list(map(lambda x: (s[x], x), values)))
            T = []
            for _, index in New:
                heappush(T, index)
            i = 0
            while T: 
                index = heappop(T)
                array[index] = New[i][0]
                i += 1
        return "".join(array)