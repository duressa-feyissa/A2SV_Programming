class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = defaultdict(int)
        adjacent = defaultdict(list)
        for x, y in prerequisites:
            adjacent[y].append(x)
            degrees[x] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if i not in degrees:
                queue.append(i)
        
        answer = [] 
        while queue:
            N = len(queue)
            for _ in range(N):
                popped = queue.popleft()
                answer.append(popped)
                for key in adjacent[popped]:
                    degrees[key] -= 1
                    if degrees[key] == 0:
                        queue.append(key)
        if len(answer) != numCourses:
            return False
        return True