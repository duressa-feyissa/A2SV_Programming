"""
# Definition for emp.
class emp:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, emps: List['emp'], id: int) -> int:
        adj = defaultdict(list)
        N = len(emps)
        for i in range(N):
            emp = emps[i]
            adj[emp.id].append(emp.importance)
            adj[emp.id].append(emp.subordinates)

        def dfs(ID):
            if ID not in adj or not adj[ID]:
                return 0
            add = adj[ID][0]
            for key in adj[ID][1]:
                add += dfs(key)
            return add
        return dfs(id)