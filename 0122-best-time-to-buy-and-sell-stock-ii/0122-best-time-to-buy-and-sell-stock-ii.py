class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}
        N = len(prices)
        def dp(index, stat):
            if index > N - 1:
                return 0
            state = (index, stat)
            if state in memory:
                return memory[state] 
            Max = 0
            if stat == 'B':
                Max = max(dp(index + 1, 'B'), dp(index + 1, 'S') - prices[index])
            else:
                Max = max(dp(index + 1, 'B') + prices[index], dp(index + 1, 'S'))
            memory[state] = Max
            return Max
        return dp(0, 'B')
                