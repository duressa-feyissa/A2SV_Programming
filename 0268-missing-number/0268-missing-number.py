class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        LENGTH = len(nums) + 1
        data = set(nums)
        
        for number in range(0, LENGTH):
            if number in data:
                pass
            else:
                return number
            
        