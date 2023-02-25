class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        index = 0
        while index < n:
            if path[index] == "." and stack and stack[-1] == "/":
                if index < n - 2 and path[index + 1] == "." and path[index + 2] != "/":
                    stack.append(".." + path[index + 2])
                    index += 2
                elif index < n - 1 and path[index + 1] != "." and path[index + 1] != "/":
                    stack.append("." + path[index + 1])
                    index += 1                   
                elif index < n - 1 and path[index + 1] == ".":
                    count = 0
                    while stack:
                        if stack[-1] == "/":
                            count += 1
                        if count == 2 or len(stack) == 1:
                            break
                        stack.pop()
                    index += 1                
            elif stack and stack[-1] == "/" and path[index] == "/":
                 pass            
            else:             
                stack.append(path[index])
            index += 1
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        return "".join(stack)
        