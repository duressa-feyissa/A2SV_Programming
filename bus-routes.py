class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        check = list(map(set, routes))
        queue = deque([])
        N = len(routes)
        T = set()
        visited = set()
        
        for i in range(N):
            if  source in check[i]:
                if source == target:
                    return 0
                for j in range(len(routes[i])):
                    queue.append((routes[i][j], i))
                visited.add(i)
        count = 0
        while queue:
            M = len(queue)
            count += 1
            for _ in range(M):
                val, index = queue.popleft()
                if val == target:
                    return count
                for i in range(N):
                    if val in check[i] and i not in visited and i != index:
                        for j in range(len(routes[i])):
                            queue.append((routes[i][j], i))
                        visited.add(i)
            
        return -1