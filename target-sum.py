class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = {}
        N = len(nums)
        def dp(index, add):
            if index >= N:
                if add == target:
                    return 1
                return 0
            state = (index, add)
            if state not in memory:
                memory[state] = dp(index + 1, add + nums[index])
                memory[state] += dp(index + 1, add - nums[index])
            return memory[state]
        return dp(0, 0)