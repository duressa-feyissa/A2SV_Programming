class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        hold, free = 0, 0
        for i in range(N-1, -1, -1):
            hold = max(free - prices[i], hold)
            free = max(hold + prices[i], free)
        return hold        