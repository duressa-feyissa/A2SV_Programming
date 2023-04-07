class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        gcf = 0
        for k in counter:
            gcf = gcd(counter[k], gcf)
        if gcf == 1:
            return False
        return True