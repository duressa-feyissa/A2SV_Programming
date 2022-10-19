class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new = set()
        j = 0
        res = 0
        for i in range(len(s)):
            while s[i] in new:
                new.remove(s[j])
                j+=1
            new.add(s[i])
            res = max(res,i-j+1)
        return res
