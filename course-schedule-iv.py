class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        indegrees = defaultdict(int)
        graph = defaultdict(list)
        dependecies = defaultdict(set)
        N = len(prerequisites)
        for i in range(N):
            indegrees[prerequisites[i][1]] += 1
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        
        queue = deque([])
        for key in range(numCourses):
            if indegrees[key] == 0:
                queue.append(key)
        while queue:
            popped = queue.popleft()
            for node in graph[popped]:
                indegrees[node] -= 1
                dependecies[node].update(dependecies[popped])
                dependecies[node].add(popped)
                if indegrees[node] == 0:
                    queue.append(node)
        answer = []
        for x, y in queries:
            if x in dependecies[y]:
                answer.append(True)
            else:
                answer.append(False)
        return answer