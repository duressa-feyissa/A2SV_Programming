class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 1
        right = max(nums)
        valid = 0
        
        while left <= right:
            
            middle = (left + right) // 2
            
            add = 0
            for num in nums:
                add += ceil(num/middle)

            if add <= threshold:
                valid = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return valid
        