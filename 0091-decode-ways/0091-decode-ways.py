class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)
        dp[N] = 1

        for i in range(N - 1, -1, -1):
            if s[i] != "0":
                dp[i] += dp[i + 1]
                if i + 1 < N and int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]
