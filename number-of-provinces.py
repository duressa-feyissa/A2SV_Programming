class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjacent = defaultdict(list)
        ROWS, COLS = len(isConnected), len(isConnected[0])
        for i in range(ROWS):
            for j in range(COLS):
                if isConnected[i][j]:
                    adjacent[i + 1].append(j + 1)
        count = 0
        check = set()
        def dfs(current, check):
            check.add(current)
            for key in adjacent[current]:
                if key not in check:
                    dfs(key, check)
                    
        for key in adjacent:
            if key not in check:
                dfs(key, check)
                count += 1
        
        return count