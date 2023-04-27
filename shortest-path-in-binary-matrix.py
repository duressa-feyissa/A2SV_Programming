class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length = len(grid)
        directions = [[-1,0], [1, 0], [0, 1], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
        visited = set()
        queue = deque([])
        
        def inbound(r, c):
            return 0 <= r < length and 0 <= c < length
        
        count = -1 
        if grid[0][0] == 0:
            queue.append((0,0))
            visited.add((0,0))
            count += 1
        reach = False
        while queue:
            if not reach:
                count += 1
            N = len(queue)
            for _ in range(N):
                popped = queue.popleft()
                if popped[0] == length - 1 and popped[1] == length - 1:
                    reach = True
                for x, y in directions:
                    row = x + popped[0]
                    col = y + popped[1]
                    if inbound(row, col) and (row, col) not in visited and not grid[row][col]:
                        queue.append((row, col))
                        visited.add((row, col))

        if reach:
            return count
        return -1