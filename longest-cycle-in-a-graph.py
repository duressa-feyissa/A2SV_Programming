class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        N = len(edges)
        starts = []
        indegree = Counter()
        for i in range(N):
            if edges[i] != -1:
                graph[i].append(edges[i])
                indegree[edges[i]] += 1

        for i in range(N):
            if indegree[i] == 0:
                starts.append(i)

        colors = [0] * N
        Max = -1
        distance = [0] * N

        def dfs(current, level):
            nonlocal Max
            if colors[current] == 2:
                return
            if colors[current] == 1:
                return
            colors[current] = 1
            distance[current] = level
            for node in graph[current]:
                if colors[node] == 1:
                    Max = max(Max, abs(distance[node] - level) + 1)
                dfs(node, level + 1)
            colors[current] = 2
        
        for start in starts:
            dfs(start, 1)   
        return Max