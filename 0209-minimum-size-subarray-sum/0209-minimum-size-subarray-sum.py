class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        smin = n
        window = 0
        found = False
        while right < n:
            if window < target:
                window += nums[right]            
                right += 1
            else:
                smin = min(smin, right - left)
                window -= nums[left]
                left += 1
                found = True
        while left < n and window >= target:
            found = True
            smin = min(smin, right - left)
            window -= nums[left]
            left += 1
            
        if found:
            return smin
        return 0
                
                
        
        