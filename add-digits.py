class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 > 0:
            num = sum(list(map(int, list(str(num)))))
        return num