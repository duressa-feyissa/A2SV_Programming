class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        count=0
        left=0
        LENGTH = len(nums)
        while left < LENGTH:
            while left + count < LENGTH:
                if nums[left + count] == 0:
                    count+=1
                else:
                    break
            if left + count < LENGTH:
                nums[left] = nums[left+count]
            left+=1
            
        left = LENGTH - zeros
        while left < LENGTH:
            nums[left] = 0
            left+=1
        
            
        