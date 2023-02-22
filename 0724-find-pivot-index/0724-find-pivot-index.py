class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum = 0
        total = sum(nums)
        for i in range(len(nums)):
            if total - prefixsum == prefixsum + nums[i]:
                return i
            prefixsum += nums[i]
        return -1
        