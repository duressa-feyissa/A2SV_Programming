class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                j+=1
            i+=1
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[count] = nums[i]
                count+=1
            i+=1
        j = len(nums) - j
        while j < len(nums):
            nums[j] = 0
            j+=1
