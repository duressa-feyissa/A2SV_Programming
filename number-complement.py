class Solution:
    def findComplement(self, num: int) -> int:
        compliment = ''
        while num:
            compliment += str((num & 1 ) ^ 1)
            num = num >> 1
        compliment = compliment[::-1]
        return int(compliment, 2)