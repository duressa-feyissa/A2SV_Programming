class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        MAP = {'}': '{', ']': '[', ')': '('}
        
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if stack and MAP[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True
        
        