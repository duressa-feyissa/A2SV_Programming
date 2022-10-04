class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = 0
        new = []
        nums = len(s)
        while i < nums:
            if s[i] == "(":
                new.append(i)
            if s[i] == ")":
                last = len(new) - 1
                j = i - new[last]
                x = s[0:new[last]]
                y = s[new[last]+1:new[last]+j]
                y = y[::-1]
                z = s[new[last]+j+1:]
                s = x + y + z
                new.pop()
                i -= 2
                nums = len(s)
            i += 1
        return s

        
            
        
        
