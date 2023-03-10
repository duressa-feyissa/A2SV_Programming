class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def backTrack(i, combination):
            if len(combination) == k:
                answer.append(combination[:])
                return
            
            if i == n:
                return
            
            for j in range(i, n):
                combination.append(j + 1)
                backTrack(j + 1, combination)
                combination.pop()

        backTrack(0, [])    
        return answer
        
