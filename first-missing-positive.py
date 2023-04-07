class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1 and nums[i] > 0 and nums[i] <= n:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i] 
                if nums[i] == nums[index]:
                    break
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1