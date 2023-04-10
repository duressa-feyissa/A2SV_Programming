class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjacent = defaultdict(list)
        n = len(graph)
        for i in range(n):
            adjacent[i].extend(graph[i])
        answer = []
        
        def dfs(current, path):
            if current == n - 1:
                answer.append(path[:])
                return
            for i in adjacent[current]:
                path.append(i)
                dfs(i, path)
                path.pop()
        dfs(0, [0])
        return answer
        
            
            
        
        
        
                