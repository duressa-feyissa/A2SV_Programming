class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        queue = deque([])
        visited = set()
        directions = [[-1,0], [1, 0], [0, 1], [0, -1]]

        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r, c))

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        while queue:
            N = len(queue)
            for _ in range(N):
                popped = queue.popleft()
                for x, y in directions:
                    r = x + popped[0]
                    c = y + popped[1]
                    if inbound(r, c):
                        if (r, c) not in visited:
                            queue.append((r,c))
                            visited.add((r,c))
                            if mat[r][c]:
                                mat[r][c] += mat[popped[0]][popped[1]] 

        return mat