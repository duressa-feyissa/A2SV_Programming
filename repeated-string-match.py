class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
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
            return lps + [0]
        lps = LPS(b)
        i, j, count = 0, 0, 0
        M, N = len(a), len(b)
        stat = False
        while j < N and count < ((N// M))  + 2:
            if i == M:
                i %= M
                count+=1
            if a[i] == b[j]:
                if j == N - 1:
                    stat = True  
                i= i + 1
                j+=1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        if not stat: return -1

        return count + 1