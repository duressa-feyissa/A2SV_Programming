class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        option1 = nums[0] * nums[1] * nums[-1]
        option2 = nums[-3] * nums[-2] * nums[-1]
        return max(option1, option2)
        
            
            
            
                
                
        
        
        