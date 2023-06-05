class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        memory = {}
        
        def dp(i, state):
            if i > N - 1:
                return 0
            if (i, state) in memory:
                return memory[(i, state)]
            
            balance = 0
            if state:
                val1 = dp(i + 1, state)
                val2 = dp(i + 1, state ^ 1) - prices[i] - fee
                balance = max(val1, val2)
            else:
                val1 = dp(i + 1, state)
                val2 = dp(i + 1, state ^ 1) + prices[i]
                balance = max(val1, val2)
            
            memory[(i, state)] = balance 
            return balance
        
        return dp(0, 1)