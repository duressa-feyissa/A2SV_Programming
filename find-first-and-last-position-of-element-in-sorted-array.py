class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        length = len(nums) 
        right = length - 1
        found = False
        index = [-1, -1]

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        if nums and nums[left] == target:
            index[0] = left

        left = 0
        right = length - 1
        middle = 0
        while left < right:
            middle = (left + right) // 2
            
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle
        
        if nums and nums[right] == target:
            index[1] = right
        elif nums and nums[right - 1] == target:
            index[1] = right - 1

        return index