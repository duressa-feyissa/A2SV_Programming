class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        
        graph = defaultdict(list)
        indegree = Counter()
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        queue = deque([])
        visited = set()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
                visited.add(i)
    
        answer = []
        while queue:
            answer.clear()
            N = len(queue)
            for _ in range(N):
                current = queue.popleft()
                answer.append(current)
                for node in graph[current]:
                    indegree[node] -= 1
                    if indegree[node] == 1 and node not in visited:
                        queue.append(node)
                        visited.add(node)
        return answer