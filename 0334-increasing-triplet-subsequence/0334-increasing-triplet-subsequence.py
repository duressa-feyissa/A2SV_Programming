class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minIndex, maxIndex = 0, -1
        length = len(nums)
        firstTwo = []
        for index in range(length):
            if firstTwo and nums[firstTwo[-1]] < nums[index]:
                return True
            if nums[minIndex] > nums[index]:
                if maxIndex != -1:
                    fistTwo = [minIndex, maxIndex]
                else:
                    fistTwo = []
                minIndex = index
                maxIndex = -1
            elif maxIndex == -1 and nums[index] > nums[minIndex]:
                maxIndex = index
                firstTwo = [minIndex, maxIndex]
            elif maxIndex != -1 and nums[index] > nums[minIndex] and nums[index] < nums[maxIndex]:
                firstTwo = [minIndex, index]
                maxIndex = index
        return False
                
            
        
        