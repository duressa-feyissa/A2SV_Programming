class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        for i in range(0,N, 2):
            if i + 1 < N and nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]