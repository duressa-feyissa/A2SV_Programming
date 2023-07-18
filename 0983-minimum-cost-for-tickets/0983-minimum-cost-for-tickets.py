class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        memory = {}
        def dp(index, span):
            if index > N - 1:
                return 0
            Min = float('inf')
            state = (index, span)
            if state in memory:
                return memory[state]
            if span > days[index]:
                Min = min(Min, dp(index + 1, span))
            Min = min(Min, dp(index + 1, days[index] + 1) + costs[0]) 
            Min = min(Min, dp(index + 1, days[index] + 7) + costs[1])
            Min = min(Min, dp(index + 1, days[index] + 30) + costs[2])
            memory[state] = Min
            return Min
        return dp(0,0)
            
        