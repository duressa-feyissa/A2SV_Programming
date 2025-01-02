class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        check = set(list(jewels))
        count = Counter()
        
        for stone in stones:
            if stone in check:
                count[stone] += 1
            
        return sum(count.values())