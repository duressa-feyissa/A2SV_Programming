class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        answer = []
        size = len(nums)
        for i in range(size):
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(size):
            if nums[i] != i + 1:
                answer.extend([nums[i], i + 1])
                break

        return answer