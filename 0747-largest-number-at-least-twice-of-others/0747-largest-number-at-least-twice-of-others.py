class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        for item in nums:
            if item != largest and largest < item * 2:
                return -1
        return nums.index(largest)
                