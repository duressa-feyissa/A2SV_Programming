class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maximum = max(arr)
        maxIndex = arr.index(maximum)
        length = len(arr)
        #check if maximum number is at the beginning or end
        if maxIndex == 0 or maxIndex == length - 1:
            return False 
        for index, value in enumerate(arr):         
            if index < maxIndex and index < length - 1:
                if value >= arr[index + 1]:
                    return False
            elif index > maxIndex:
                if value >= arr[index - 1]: 
                    return False
        return True

        