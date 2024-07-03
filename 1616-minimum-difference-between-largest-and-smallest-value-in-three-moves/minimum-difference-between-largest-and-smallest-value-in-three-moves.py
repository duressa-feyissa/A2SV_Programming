class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        if N < 5:
            return 0
        Min = float('inf')
        Min = min(Min, nums[-1] - nums[3])
        Min = min(Min, nums[-4] - nums[0])
        Min = min(Min, nums[-2] - nums[2])
        Min = min(Min, nums[-3] - nums[1])
            
        return Min
    


        
        
        
        
        