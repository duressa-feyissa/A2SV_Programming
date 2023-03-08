class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = 0
        n = len(arr)
        right = n - 1
        
        while left <= right:
            
            middle = (right + left) // 2
            
            if middle == 0:
                left = middle + 1
            elif middle == n - 1:
                right = middle - 1
            elif arr[middle] > arr[middle + 1] and arr[middle] > arr[middle - 1]:
                return middle
            elif arr[middle] < arr[middle + 1] and arr[middle] > arr[middle - 1]:
                left = middle + 1
            elif arr[middle] > arr[middle + 1] and arr[middle] < arr[middle - 1]:
                right = middle - 1
        
                
        