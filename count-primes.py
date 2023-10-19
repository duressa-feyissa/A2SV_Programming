class Solution:
    def countPrimes(self, n: int) -> int:
        N = ceil(sqrt(n))
        array = [1] * n
        for i in range(2, N):
            if array[i]:
                for j in range(i * i, n, i):
                    array[j] = 0
        count = 0
        for i in range(2, n):
            if array[i]:
                count += 1
        return count