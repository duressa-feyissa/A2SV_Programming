class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                i += 2
                j += 2
            else:
                return nums[i]
        return nums[i]
                
        