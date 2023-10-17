class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[1,1] for _ in range(N)]
        Max = 0
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if nums[i] < nums[j]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = 0
                    if dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
            Max = max(Max, dp[i][0])
        result = 0
        for i in range(N):
            if dp[i][0] == Max:
                result += dp[i][1]
        return result