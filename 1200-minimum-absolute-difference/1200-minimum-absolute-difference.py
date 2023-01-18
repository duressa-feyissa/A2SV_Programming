class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        smalldiff = float('inf')
        for i in range(1, len(arr)):
            smalldiff = min(arr[i] - arr[i - 1], smalldiff)
        answer = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == smalldiff:
                answer.append([arr[i-1],arr[i]])
        return answer
            
        