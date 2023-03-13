class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def backTrack(i, stack): 
            if i == n:        
                if len(stack) >= 2:
                    return True
                return False
            ans = False
            for j in range(i, n):
                temp = int(s[i:j + 1])
                if not stack or stack[-1] - temp == 1:
                    stack.append(temp)
                    ans = ans or backTrack(j + 1, stack)
                    stack.pop()
                
            return ans
        return backTrack(0, [])
        
                
                    
                    
            
            
        