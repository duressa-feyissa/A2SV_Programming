class Solution:
    def integerReplacement(self, n: int) -> int:
        memory = {}
        def dp(num):
            if num == 1:
                return 0
            if num in memory:
                return memory[num]
            if num % 2 == 0:
                memory[num] = dp(num // 2) + 1
            else:
                memory[num] = min(dp(num + 1), dp(num - 1)) + 1
            return memory[num]
        return dp(n)
        