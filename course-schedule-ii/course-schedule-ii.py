class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = Counter()
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            inDegree[y] += 1
            graph[x].append(y)
            
        queue = deque([])
        visited = set()
        
        for key in range(numCourses):
            if inDegree[key] == 0:
                queue.append(key)
                visited.add(key)
        ans = []
        while queue:
            N = len(queue)
            for _ in range(N):
                popped = queue.popleft()
                ans.append(popped)
                for n in graph[popped]:
                    inDegree[n] -= 1
                    if inDegree[n] <= 0 and n not in visited:
                        queue.append(n)
                        visited.add(n)
        if len(ans) != numCourses:
            return []
        return ans[::-1]
                        
                        
        
        
            
        
        