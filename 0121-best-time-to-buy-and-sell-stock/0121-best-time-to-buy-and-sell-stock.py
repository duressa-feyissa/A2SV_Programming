class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        memory = {}
        def dp(index, stat):
            if index >= N:
                return 0
            state = (index, stat)
            if state in memory:
                return memory[state]
            if stat == 1:
                memory[state] = max(dp(index + 1, stat), dp(index + 1, stat ^ 1) - prices[index])
            else:
                memory[state] = max(dp(index + 1, stat), prices[index])
            return memory[state]
        return dp(0, 1)
                

        
            
            
        