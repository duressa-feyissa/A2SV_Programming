class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        dividor = 2
        while n != 1:
            if n % dividor == 0:
                n = n // dividor
                count += dividor
            else:
                dividor += 1
        return count