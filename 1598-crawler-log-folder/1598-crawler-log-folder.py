class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            n = len(log)
            if n == 2 and log == "./":
                pass
            elif n == 3 and log == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(log)

        return len(stack)
                
                
            
            
        
        
        