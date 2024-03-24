class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while nums[i] != i + 1:
                correctPosition = nums[i] - 1
                if nums[i] == nums[correctPosition]:
                    return nums[i]
                nums[correctPosition], nums[i] = nums[i], nums[correctPosition]