class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n  = len(board),len(board[0])
        visited = set()

        def dfs(r,c,i):
            if i==len(word):
                return True

            if r<0 or r==m or c<0 or c==n or (r,c) in visited or board[r][c]!=word[i]:
                return False
            
            visited.add((r,c))

            if dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1):
                return True

            visited.remove((r,c))
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x,y,0):
                    return True
        
        return False
