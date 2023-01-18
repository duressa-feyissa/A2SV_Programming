class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        answer = -1
        for index in range(len(nums)):
            if nums[index] != largest and largest < nums[index] * 2:
                return -1
            if nums[index] == largest:
                answer = index
        return answer
                