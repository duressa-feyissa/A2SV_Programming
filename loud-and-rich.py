class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x, y in richer:
            graph[x].append(y)
            indegree[y] += 1
        N =len(quiet)
        MinOrder = list(range(N))
        queue = deque([])
        
        answer = list(range(N))
        for i in range(N):
            if indegree[i] == 0:
                queue.append((i, i))
                MinOrder[i] = i
        while queue:
            current, minIndex = queue.popleft()
            answer[current] = minIndex          
            for node in graph[current]:
                indegree[node] -= 1
                if quiet[node] < quiet[minIndex]:
                    minIndex = node
                if quiet[minIndex] < quiet[MinOrder[node]]:
                    MinOrder[node] = minIndex
                if indegree[node] == 0:
                    queue.append((node, MinOrder[node]))
        return MinOrder