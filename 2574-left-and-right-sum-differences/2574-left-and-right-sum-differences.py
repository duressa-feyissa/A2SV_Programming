class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        answer = []
        for num in nums:
            right = total - left - num
            answer.append(abs(left - right))
            left += num
        return answer
            