class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = 27
        checker = 0
        add = 0
        if len(needle) > len(haystack):
            return -1

        window = len(needle)
        for i in range(len(needle)):
            checker *= a
            checker += (ord(needle[i]) - ord('a'))
            add *= a
            add += (ord(haystack[i]) - ord('a'))
        if checker == add:
            return 0
        k = len(needle)
        for i in range(len(needle), len(haystack)):
            if add == checker:
                return i - k
            add -=  (ord(haystack[i - k]) - ord('a')) * (a ** (k - 1))
            add *= a
            add += (ord(haystack[i]) - ord('a'))
        if checker == add:
            return len(haystack) - k
        return -1