class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        memory = [-1] * (amount + 1)
        memory[0] = 0
        for i in range(1, amount + 1):
            minimum = float('inf')
            for j in range(N):
                if i - coins[j] > -1  and memory[i - coins[j]] != -1:
                    minimum = min(minimum, memory[i - coins[j]] + 1) 
            if float('inf') != minimum:
                memory[i] = minimum
        return memory[amount]
                    
        