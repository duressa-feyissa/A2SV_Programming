class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x, y in edges:
            graph[x].append(y)
            indegree[y] += 1
        
        queue = deque([])
        for key in range(n):
            if indegree[key] == 0:
                queue.append(key)

        answer = defaultdict(set)
        while queue:
            current = queue.popleft()
            for node in graph[current]:
                indegree[node] -= 1
                answer[node].update(answer[current])
                answer[node].add(current)
                if indegree[node] == 0:
                    queue.append(node)
        
        result = []
        for key in range(n):
            if key not in answer:
                result.append([])
            else:
                result.append(sorted(answer[key]))
        return result