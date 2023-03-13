class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        stat = False
        def backTrack(i, stack): 
            nonlocal stat
            if i == n:        
                if len(stack) >= 2:
                    stat = True
                return
            
            for j in range(i, n):
                temp = int(s[i:j + 1])
                if not stack or stack[-1] - temp == 1:
                    backTrack(j + 1, stack + [temp])
        
        backTrack(0, [])
        return stat