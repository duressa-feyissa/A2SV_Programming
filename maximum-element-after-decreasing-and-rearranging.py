class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        N = len(arr)
        state = 1
        arr[0] = 1
        for i in range(1,N):
            if abs(arr[i - 1] - arr[i]) > 1:
                arr[i] = arr[i - 1] + 1    
        return arr[-1]