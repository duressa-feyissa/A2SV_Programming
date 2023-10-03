class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        N = len(s) 
        for i in range(N):
            if stack:
                if stack[-1][0] == s[i]:
                    stack[-1][1] += 1
                else:
                    stack.append([s[i], 1])
            else:
                stack.append([s[i], 1])
            while stack and stack[-1][1] == k:
                stack.pop()
        
        return "".join(list(map(lambda x: x[0] * x[1], stack)))
                