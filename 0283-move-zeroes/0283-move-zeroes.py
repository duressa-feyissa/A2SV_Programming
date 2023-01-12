class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        left = 0
        track = 0
        while left < len(nums):
            if nums[left] != 0:
                nums[track] = nums[left]
                track+=1
            left+=1
        
        left = len(nums) - zeros
        while left < len(nums):
            nums[left] = 0
            left += 1
            
    
            
        
        
