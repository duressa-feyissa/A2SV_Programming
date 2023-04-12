class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[-1,0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(image), len(image[0])
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(row, col, initial):
            visited[row][col] = 1
            image[row][col] = color
            for x, y in directions:
                r = row + x
                c = col + y
                if inbound(r, c):
                    if visited[r][c] == 0 and image[r][c] == initial:
                        dfs(r, c, initial)
        
        if inbound(sr, sc):
            dfs(sr, sc, image[sr][sc])
        
        return image