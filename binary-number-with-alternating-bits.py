class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n:
            curr = n & 1
            if prev == curr:
                return False
            prev = curr
            n = n >> 1
        return True