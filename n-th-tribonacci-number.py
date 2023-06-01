class Solution:
    def tribonacci(self, n: int) -> int:
        prev1, prev2, prev3 = 0, 1, 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(3, n + 1):
            T = prev3
            prev3 = prev1 + prev2 + prev3
            prev1 = prev2
            prev2 = T
            
        return prev3