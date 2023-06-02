class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 4:
            return max(nums)
        def dp(i, memory, N):
            if i >= N:
                return 0
            if i in memory:
                return memory[i]
            Max = max(nums[i] + dp(i + 2, memory, N),  dp(i + 1, memory, N))
            memory[i] = Max
            return Max
        return max(dp(0, {}, N - 1), dp(1, {}, N))