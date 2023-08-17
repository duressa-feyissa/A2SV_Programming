class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        add = 0
        for i in range(N):
            if i % 2 == 0:
                add += nums[i]
        return add
            