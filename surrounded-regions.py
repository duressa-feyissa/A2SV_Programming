class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1,0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        def dfs(row, col, action):
            visited[row][col] = 1
            if action:
                board[row][col] = 'X'
            for x, y in directions:
                r = row + x
                c = col + y
                if inbound(r, c):
                    if visited[r][c] == 0 and board[r][c] == 'O':
                        dfs(r, c, action)
        
        for i in [0, ROWS - 1]: 
            for j in range(COLS):
                if board[i][j] == 'O' and not visited[i][j]:
                    dfs(i, j, 0)
        
        for i in [0, COLS - 1]: 
            for j in range(ROWS):
                if board[j][i] == 'O' and not visited[j][i]:
                    dfs(j, i, 0)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and not visited[i][j]:
                    dfs(i, j, 1)