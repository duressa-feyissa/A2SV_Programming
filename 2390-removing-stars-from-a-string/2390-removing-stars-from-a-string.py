class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        answer = ""
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
            