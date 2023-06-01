class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        memory = {}
        def dp(i):
            if i == N - 1 or i == N - 2:
                return cost[i] 
            if i in memory:
                return memory[i]
            memory[i] = min(dp(i + 1) + cost[i], dp(i + 2) + cost[i])
            return memory[i]
        return min(dp(0), dp(1))