class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adjacent = defaultdict(list)
        N = len(parent)
        for i in range(1,N):
            adjacent[parent[i]].append(i)
            adjacent[i].append(parent[i])
        Max = 0
        visited = set()
        def dfs(current):
            nonlocal Max
            count = 0
            visited.add(current)
            tracker = {}
            for node in adjacent[current]:
                if node not in visited:
                    res = dfs(node)
                    if s[current] != s[node]:
                        tracker[node] = res
            C = len(tracker)
            values = sorted(tracker.values())
            if C > 1:
                count = values[-1] + values[-2] + 1
            elif C == 1:
                count = values[0] + 1
            else:
                count = 1
            Max = max(Max, count)
            return values[-1] + 1 if C > 0 else 1
        dfs(0)
        return Max
                
        
        
        
        