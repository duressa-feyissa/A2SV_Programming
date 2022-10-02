class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        start = 0
        end = len(piles) - 1
        piles.sort()
        while True:
            piles[end] = 0
            piles[start] = 0
            if end - start == 2:
                break
            end -= 2
            start += 1
        return sum(piles)
