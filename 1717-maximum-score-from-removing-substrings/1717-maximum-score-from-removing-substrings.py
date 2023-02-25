class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            first, second = "a", "b"
        else:
            first, second = "b", "a"
        
        point = 0
        stack1, stack2 = [], []
        
        for char in s:
            if char == second and stack1 and stack1[-1] == first:
                point += max(x, y)
                stack1.pop()
            else:
                stack1.append(char)
                
        for char in stack1:
            if char == first and stack2 and stack2[-1] == second:
                point += min(x, y)
                stack2.pop()
            else:
                stack2.append(char)
        
        return point
        
                
                
        
        
            
        
        