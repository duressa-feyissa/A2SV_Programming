class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        r = len(heights)
        c = len(heights[0])
        visited = set()

        def inbound(i, j):
            return 0 <= i < r and 0 <= j < c
        
        direction = [(-1,0),(1,0),(0,1),(0,-1)]

        arr = []

        heappush(arr,(0, 0, 0))

        while arr:

            distance , row , col = heappop(arr)

            if (row, col) in visited:
                continue
            
            if row >= r-1 and col >= c-1:
                return distance
            
            visited.add((row, col))

            for xpos , ypos in direction:

                n_r = row + xpos 
                n_c = col + ypos

                if inbound(n_r, n_c):
                    res = abs(heights[n_r][n_c] - heights[row][col])
                    heappush(arr, (max(distance, res), n_r, n_c))