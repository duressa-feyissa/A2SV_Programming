class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = arr[-1]
        answer = [0] * len(arr)
        answer[-1] = -1
        
        for index in range(len(arr) - 2, -1, -1):
            answer[index] = maximum
            maximum = max(maximum, arr[index])
        return answer