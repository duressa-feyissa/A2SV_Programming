class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0
        zeros = nums.count(0)
        track = 0
        left = 0
        while left < len(nums):
            if nums[left] != 0:
                nums[track] = nums[left]
                track += 1
            left += 1
            
        left = len(nums) - zeros
        while left < len(nums):
            nums[left] = 0
            left += 1
        return nums
                
        
                
        
        