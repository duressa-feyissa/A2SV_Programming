class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        check, window = 0, 0
        for i in range(m):
            check += hash(s1[i])
            if i < m - 1: 
                window += hash(s2[i])

        for i in range(m-1, n):
            window += hash(s2[i])
            if window == check:
                return True
            window -= hash(s2[i - m + 1])
        return False

            