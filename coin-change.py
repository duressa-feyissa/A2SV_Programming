class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        coins.sort()
        coins.reverse()
        memory = {}
        def helper(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in memory:
                return memory[amount]
            Min = float('inf')
            for i in range(N):
                change = amount - coins[i]
                Min = min(helper(change), Min)
            memory[amount] = Min + 1
            return memory[amount]
        val = helper(amount)
        return val if val != float('inf') else -1