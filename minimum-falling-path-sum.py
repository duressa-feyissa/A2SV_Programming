class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        memory = {}
        def inbound(r, c):
            return 0 <= c < N
        dirs = [(1,0), (1,1), (1,-1)]
        def dp(r, c):
            if r > N - 1:
                return 0
            state = (r, c)
            if state in memory:
                return memory[state]
            Min = float('inf')
            for x, y in dirs:
                nr, nc = x + r, y + c
                if inbound(nr, nc):
                    Min = min(Min, dp(nr, nc) + matrix[r][c])
            memory[state] = Min
            return Min
        Min = float('inf')
        for i in range(N):
            Min = min(dp(0,i), Min)
        return Min