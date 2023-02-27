class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == ")":
                popped = stack.pop()
                if popped == 0:
                    stack[-1] += 1
                else:
                    stack[-1] +=  (popped  * 2)               
            else:
                stack.append(0)
                
        return stack[0]