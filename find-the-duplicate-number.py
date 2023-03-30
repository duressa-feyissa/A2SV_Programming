class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        answer = []
        n = len(nums)
        left = 0
        while left < n:
            if nums[left] == left + 1:
                left += 1
            else:
                correctPosition = nums[left] - 1
                if correctPosition != left and nums[correctPosition] == nums[left]:
                    return nums[left]
                else:
                    nums[correctPosition], nums[left] = nums[left], nums[correctPosition]