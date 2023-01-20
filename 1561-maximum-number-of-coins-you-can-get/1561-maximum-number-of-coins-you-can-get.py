class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 2
        result = 0
        while left < right:
            left+=1
            result+=piles[right]
            right-=2
        return result
            
            
            
        