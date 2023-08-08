from typing import List
from collections import *
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]):
        graph = defaultdict(list)
        indegree = Counter()
        for x, y in edges:
            graph[x].append(y)
            indegree[y] += 1
        
        queue = deque([])
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        answer = [1] * n
        time = 1
        while queue:
            N = len(queue)
            for _ in range(N):
                current = queue.popleft()
                answer[current - 1] = time
                for node in graph[current]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        queue.append(node)
            time += 1
    
        return answer