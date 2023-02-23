class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k-1])
        ans = float('-inf')
        left = 0
        
        for right in range(k-1, len(nums)):
            window += nums[right]
            ans = max(ans, window/k)
            window -= nums[left]
            left += 1
        
        return ans
            
            
            
            
        
        