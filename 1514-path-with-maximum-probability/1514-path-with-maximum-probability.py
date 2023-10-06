class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    
        distances = {node: float('-inf') for node in range(n)}
        distances[start_node] = 1
        visited = set()
        
        graph = defaultdict(list)    
        M = len(edges)
        for i in range(M):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
            
        queue = [(-1, start_node)]
        while queue:
            current_distance, current_node = heappop(queue)
            current_distance = -current_distance
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in graph[current_node]:
                distance = current_distance * weight
                if distance > distances[neighbor]:
                    distances[neighbor] = distance
                heappush(queue, (-distance, neighbor))
        if distances[end_node] == float('-inf'):
            return 0
        return distances[end_node]
        
            
                
        