class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = [-1] * n
        answer = []
        for i in range(n):
            array[nums[i] - 1] = nums[i]
        for i in range(n):
            if array[i] == -1:
                answer.append(i + 1)
        return answer