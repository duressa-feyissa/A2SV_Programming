class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        answer = 0
        checker = set()
        N = len(s)
        while right < N:
            if s[right] in checker:
                checker.remove(s[left])
                left += 1
            else:
                checker.add(s[right])
                right += 1
            answer = max(answer, right - left)
        return answer
