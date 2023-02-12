class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = 0
        s = s.rstrip()
        for i in range(len(s)):
            if s[i] == " ":
                last = i + 1
        return len(s[last:])
        