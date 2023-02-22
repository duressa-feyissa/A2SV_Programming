class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        cur_sum = 0
        n = len(nums)
        ans = n + 1

        for right in range(n):
            cur_sum += nums[right]
                
            while cur_sum >= target:
                ans = min(ans, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                
        if ans != n + 1:
            return ans
        return 0
        
        
        