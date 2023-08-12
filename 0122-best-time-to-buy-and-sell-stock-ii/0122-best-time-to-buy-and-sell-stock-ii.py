class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        memory = [[0,0] for _ in range(N+1)]
        for i in range(N-1, -1, -1):
            memory[i][0] = max(memory[i+1][1] - prices[i], memory[i+1][0])
            memory[i][1] = max(memory[i+1][0] + prices[i], memory[i+1][1])
        return memory[0][0]

        