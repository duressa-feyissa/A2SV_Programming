class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        for i in command:
            if i != ")":
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append("o")
                elif stack[-1] == "G":
                    pass
                else:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append("a")
                    stack.append("l")
        s = ""
        for i in stack:
            s+=i
        return s
                    
                    
        