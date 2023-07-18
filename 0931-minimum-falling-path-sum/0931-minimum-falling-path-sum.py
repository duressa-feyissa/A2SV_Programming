class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        memory = [0] * N
        for i in range(N-1,-1,-1):
            next = [0] * N
            for j in range(N):
                Min = float('inf')
                if j - 1 > -1:
                    Min = min(memory[j - 1], Min)
                if j + 1 < N:
                    Min = min(memory[j + 1], Min)
                Min = min(memory[j], Min)
                next[j] = Min + matrix[i][j]
            memory = next
        return min(memory)
                    
                    
                    
                