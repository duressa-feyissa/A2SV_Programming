class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        possibles = {
            1: [6, 8], 2: [7, 9], 3: [4, 8],
            4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6],
            8: [1, 3], 9: [2, 4], 0: [4,6]
        }

        for i in range(n-1):
            next = [0] * 10
            for j in range(10):
                for k in possibles[j]:
                    next[k] += dp[j]
            dp = next[:]
        
        return sum(dp) % (10 ** 9 + 7)