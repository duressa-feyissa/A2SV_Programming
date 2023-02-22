class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        ans = 0
        left = 0
        right = 0
        n = len(s)
        while right < n:
            if s[right] in check:
                ans = max(ans, len(check))
                check.remove(s[left])
                left += 1
            else:
                check.add(s[right])
                if right == n - 1:
                    ans = max(ans, len(check))
                right += 1
        return ans
        