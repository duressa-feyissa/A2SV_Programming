class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                result += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1
        return result
        