class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        check = set()
        counter = Counter(s)
        for char in s:
            if char not in check:
                while stack and stack[-1] > char and counter[stack[-1]] > 0:
                    popped = stack.pop()
                    check.remove(popped)
                stack.append(char)
                check.add(char)
            counter[char] -= 1
        return "".join(stack)
