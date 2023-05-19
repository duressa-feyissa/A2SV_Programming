class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {i: i for i in range(26)}
        size = {i: 1 for i in range(26)}
        unequal = {i: [] for i in range(26)}
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

        for equation in equations:
            A, sign, B = Map[equation[0]], equation[1] + equation[2], Map[equation[3]]
            repA, repB = find(A), find(B)
            if sign == "==":
                if repA != repB:
                    union(A,B)
            else:
                if repA == repB:
                    return False
                unequal[A].append(B)
                unequal[B].append(A)
        
        for A in range(26):
            for B in unequal[A]:
                if find(A) == find(B):
                    return False                 
        return True