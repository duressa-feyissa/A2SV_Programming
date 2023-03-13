class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        stat = False
        def backTrack(i, stack): 
            nonlocal stat
            if i == n:        
                if len(stack) >= 2:
                    return True
                return False
            ans = False
            for j in range(i, n):
                temp = int(s[i:j + 1])
                if not stack or stack[-1] - temp == 1:
                    ans = ans or backTrack(j + 1, stack + [temp])
            return ans
        return backTrack(0, [])
        
                
                    
                    
            
            
        