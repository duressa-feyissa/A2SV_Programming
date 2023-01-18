class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        array = sorted(nums)
        option1 = array[0] * array[1] * array[-1]
        option2 = array[-3] * array[-2] * array[-1]
        return max(option1, option2)
        
            
            
            
                
                
        
        
        