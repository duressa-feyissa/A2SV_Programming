class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        for index in range(len(nums)):
            answer.append(nums[nums[index]])
        return answer
        