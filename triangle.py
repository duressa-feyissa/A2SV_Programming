class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        length = list(map(lambda x: len(x), triangle))
        memory = {}
        def dp(r, c):
            if r >= N or c >= length[r]:
                return 0
            if (r, c) in memory:
                return memory[(r, c)]
            memory[(r,c)] = min(dp(r + 1, c), dp(r + 1, c + 1)) + triangle[r][c]
            return memory[(r, c)]
        return dp(0,0)