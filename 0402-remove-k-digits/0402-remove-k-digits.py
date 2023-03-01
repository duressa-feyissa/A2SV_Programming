class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        n = len(num)
        stack = []
        ans = ""
        for i in range(n):
            while stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
                if k == 0:
                    ans = "".join(stack) + num[i:]
                    if ans == "":
                        return "0"
                    return str(int(ans))
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1
        
        if stack:
            return str(int("".join(stack)))
        return "0"
            
            
            
            
            
            