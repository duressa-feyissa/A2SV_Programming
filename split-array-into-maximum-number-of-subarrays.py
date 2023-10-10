class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        overall = (1 << 32) - 1
        length = len(nums)
        for index in range(length):
            overall &= nums[index]
        temp = (1 << 32) - 1
        count = 0
        score = 0
        for index in range(length):
            temp &= nums[index]
            if temp == overall:
                temp = (1 << 32) - 1
                count += 1
        if overall != 0 and count > 1:
            return 1
        return count