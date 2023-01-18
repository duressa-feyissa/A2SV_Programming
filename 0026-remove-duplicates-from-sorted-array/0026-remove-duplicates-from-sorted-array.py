class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        preview = 0
        left = 1
        while left < len(nums):
            if nums[left] != nums[preview]:
                preview += 1
                nums[preview ] = nums[left]
            left += 1
        return preview + 1
        