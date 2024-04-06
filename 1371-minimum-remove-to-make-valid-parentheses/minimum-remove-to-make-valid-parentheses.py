class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        length = len(s)
        stack = []
        A = set()
        ans = []
        for i in range(length):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and stack:
                pop = stack.pop()
                A.add(pop)
                A.add(i)
        print(A)
        for i in range(length):
            if s[i] == '(' and i in A:
                ans.append(s[i])
            if s[i] == ')' and i in A:
                ans.append(s[i])
            if s[i] != '(' and s[i] != ')':
                ans.append(s[i])
        return "".join(ans)

        
        
                


        