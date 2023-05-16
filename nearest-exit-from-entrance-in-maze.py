class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS = len(maze)
        COLS = len(maze[0])
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        
        def exit(r, c):
            return 0 == r or 0 == c or r == ROWS -1 or c == COLS - 1
        
        queue = deque([(entrance[0], entrance[1])])
        visited = set()
        visited.add(tuple(entrance))
        count = 0
        while queue:
            N = len(queue)
            for _ in range(N):
                r, c = queue.popleft()
                for x, y in directions:
                    nr = x + r
                    nc = y + c
                    if inbound(nr, nc) and (nr, nc) not in visited and maze[nr][nc] == '.':
                        print(nr, nc)
                        if exit(nr, nc):
                            return count + 1
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            count += 1
        return -1