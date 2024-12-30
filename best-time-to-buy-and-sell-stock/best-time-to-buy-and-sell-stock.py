class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        N = len(prices)
        def dp(index, action):
            if index >= N:
                return 0
            
            state = (index, action)
            
            if state in memo:
                return memo[state]
            
            if action == 1:
                memo[state] = max(dp(index + 1, 1), dp(index + 1, 0) - prices[index])
            else:
                memo[state] = max(dp(index + 1, 0), prices[index])
            return memo[state]
        
        return max(dp(0, 1), 0)
                
                
            
        
        
        