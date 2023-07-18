class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}
        N = len(prices)
        def dp(index, stat):
            if index >= N:
                return 0
            state = (index, stat)
            if state not in memory:
                val1, val2 = 0, 0
                if stat == 'B':
                    val1 = dp(index + 1, 'S') - prices[index]
                    val2 = dp(index + 1, 'B')
                elif stat == 'S':
                    val1 = dp(index + 1, 'C') + prices[index]
                    val2 = dp(index + 1, 'S')
                else:
                    val1 = dp(index + 1, 'B')
                memory[state] = max(val1, val2)
            return memory[state]
        return dp(0,'B')