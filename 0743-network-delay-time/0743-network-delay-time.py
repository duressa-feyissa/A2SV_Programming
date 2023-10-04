class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, e, w in times:
            graph[s].append((e, w))
        distances = {node: float('inf') for node in range(1, n+1)}
        distances[k] = 0
        visited = set()

        queue = [(0, k)]
        while queue:
            current_distance, current_node = heappop(queue)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                heappush(queue, (distance, neighbor))
        smallestTimeToAll = max(list(distances.values()))
        if smallestTimeToAll == float('inf'):
            return -1
        return smallestTimeToAll
        


        