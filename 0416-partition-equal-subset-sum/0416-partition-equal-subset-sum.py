class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memory = {}
        N = len(nums)
        total = sum(nums)
        half = total // 2
        if total % 2 != 0:
            return False
        def dp(i, add):
            if i >= N or add <= 0:
                return add == 0
            if (i, add) not in memory:
                memory[(i, add)] = dp(i + 1, add) or dp(i + 1, add - nums[i])
            return memory[(i, add)] 
        return dp(0, half)
