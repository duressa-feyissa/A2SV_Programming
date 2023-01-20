class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        array = [0] * 3
        for i in nums:
            array[i] += 1
        index = 0
        for i in range(3):
            for j in range(array[i]):
                nums[index] = i
                index+=1

                
        