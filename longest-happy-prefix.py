class Solution:
    def longestPrefix(self, s: str) -> str:
        def LPS(s):
            M = len(s)
            lps = [0] * (M)
            i, j = 0, 1
            while j < M:
                if s[i] == s[j]:
                    lps[j] = i + 1
                    i, j= i + 1, j + 1
                else:
                    if i == 0:
                        j += 1
                    else:
                        i = lps[i - 1]
            return lps 
        lps = LPS(s)
        return s[-lps[-1]:] if lps[-1] != 0 else ""