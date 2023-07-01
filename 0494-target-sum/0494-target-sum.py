class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        N = len(nums)
        dp = [0] * ((2 * total) + 1)
        dp[nums[0] + total] = 1
        dp[-nums[0] + total] += 1
        for i in range(1, N):
            next = [0] * ((2 * total) + 1)
            for j in range(-total, total+1):
                if dp[j + total] > 0:
                    next[j + nums[i] + total] += dp[j + total]
                    next[j - nums[i] + total] += dp[j + total]
            dp = next
        return 0 if abs(S) > total else dp[S + total]