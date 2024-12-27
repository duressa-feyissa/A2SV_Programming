class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(word):
            stack = []
            for c in word:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
        
        return helper(s) == helper(t)
                    
        