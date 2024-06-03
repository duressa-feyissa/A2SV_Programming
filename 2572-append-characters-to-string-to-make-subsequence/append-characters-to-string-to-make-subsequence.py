class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left, right = 0, 0
        N, M = len(s), len(t)
        while left < N and right < M:
            if s[left] == t[right]:
                right += 1
            left += 1
        return M - right
