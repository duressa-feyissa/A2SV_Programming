class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = {}
        emails = set()
        count = 0
        N = len(accounts)
        for i in range(N):
            for j in range(1, len(accounts[i])):
                emails.add(accounts[i][j])
                names[accounts[i][j]] = accounts[i][0]
        
        rep = {e: e for e in emails}
        size = {e: 1 for e in emails}
         
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
            M = len(accounts[i])
            for j in range(1, M):
                for k in range(j + 1, M):
                    x = find(accounts[i][j])
                    y = find(accounts[i][k])
                    if x != y:
                        union(accounts[i][j], accounts[i][k])

        answer = defaultdict(list)
        for key in emails:
            parent = find(key)
            answer[parent].append(key)
        result = []
        for key in list(answer.keys()):
            T = []
            T.append(names[key])
            T.extend(sorted(answer[key]))
            result.append(T)
        return result