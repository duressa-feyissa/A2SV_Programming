class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        answer = 0
        adjacent = defaultdict(set)
        for road in roads:
            adjacent[road[0]].add(road[1])
            adjacent[road[1]].add(road[0])
        
        length = [0] * n
        for i in range(n):
            length[i] = len(adjacent[i])

        for i in range(n):
            for j in range(i + 1, n):
                cal = length[i] + length[j]
                if i in adjacent[j]:
                    cal -= 1
                answer = max(answer, cal)

        return answer