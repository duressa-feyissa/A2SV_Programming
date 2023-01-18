class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[left] = nums[index]
                left += 1
        return left
