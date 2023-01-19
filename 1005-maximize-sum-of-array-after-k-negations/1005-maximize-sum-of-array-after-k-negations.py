class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        for index in range(len(nums)):
            if k < 1:
                break
            if nums[index] < 0:
                nums[index] *= -1
                k -= 1
                if k % 2 and index == length - 1:
                    nums[index] *= -1
            else:
                if k % 2 == 1:
                    if index == 0:
                        nums[index] *= -1
                    elif nums[index - 1] > nums[index]:
                        nums[index] *= -1
                    elif nums[index - 1] <= nums[index]:
                        nums[index - 1] *= -1
                k = 0        
        return sum(nums)
            
        
        
        