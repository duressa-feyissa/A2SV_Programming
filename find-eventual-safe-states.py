class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        adjacent = defaultdict(list)
        
        for i in range(N):
            adjacent[i].extend(graph[i])
        
        colors = [0] * N
        answer = [1] * N
         
        def dfs(current):
            if colors[current] == 2:
                return True
            if colors[current] == 1:
                return False
            colors[current] = 1
            for node in adjacent[current]:
                if not dfs(node):
                    answer[current] = 0
                    return False
            colors[current] = 2
            return True
        
        for i in range(N):
            if colors[i] == 0:
                if not dfs(i):
                    answer[i] = 0

        filter = []
        for i in range(N):
            if answer[i]:
                filter.append(i)
        return filter