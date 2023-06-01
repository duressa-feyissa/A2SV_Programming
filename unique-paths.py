class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = {}
        direction = [(1, 0), (0, 1)]
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        
        def helper(r, c):
            if (r, c) == (m - 1, n - 1):
                return 1
            if (r, c) in memory:
                return memory[(r, c)]
            count = 0
            for x, y in direction:
                nr = x + r
                nc = y + c
                if inbound(nr, nc):
                    count += helper(nr, nc)
            memory[(r, c)] = count
            return memory[(r, c)]
        return helper(0,0)