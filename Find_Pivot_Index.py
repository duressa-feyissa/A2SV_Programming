class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        
        for i in range(0,len(nums)):
            if i == 0:
                x = 0
            else:
                x = nums[i-1]
            if x == nums[-1] - nums[i]:
                return i
        return -1
            
            
        
