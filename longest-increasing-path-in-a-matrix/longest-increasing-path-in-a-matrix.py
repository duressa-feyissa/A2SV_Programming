from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        M, N = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def inBound(r, c):
            return 0 <= r < M and 0 <= c < N
        
        memo = [[-1] * N for _ in range(M)]
        
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            
            max_len = 1
            for x, y in dirs:
                nx, ny = i + x, j + y
                if inBound(nx, ny) and matrix[nx][ny] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(nx, ny))
            memo[i][j] = max_len
            return max_len
        
        answer = 0
        for i in range(M):
            for j in range(N):
                answer = max(answer, dfs(i, j))
        
        return answer
