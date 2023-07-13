class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        N = len(edges)
        for i in range(N):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        visited = set()
        def dfs(curr):
            add = 0
            visited.add(curr)
            for node in graph[curr]:
                if node not in visited:
                    res = dfs(node)
                    if res:
                        add += res
            if hasApple[curr]:
                add += 1                
            else:
                if add:
                    add += 1    
            return add
        
        res = dfs(0)
        if res:
            return (res - 1) * 2
        return 0
        
        