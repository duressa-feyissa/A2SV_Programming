class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        N = len(coins)
        
        def dp(index, add):
            if add < 0 or index >= N:
                return float('inf')
            
            if add == 0:
                return 0
            
            state = (index, add)
            if state in memo:
                return memo[state]
            
            take = 1 + dp(index, add - coins[index])
            skip = dp(index + 1, add)
            memo[state] = min(take, skip)
            
            return memo[state]
        
        result = dp(0, amount)
        return result if result != float('inf') else -1
