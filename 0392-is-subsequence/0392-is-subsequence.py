class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        i = 0
        j = 0
        n = len(s)
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                if i == n:
                    return True
            else:
                j += 1
        return False