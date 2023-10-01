class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        N = len(satisfaction)
        memory = {}
        def dp(index, added):
            if index > N - 1:
                return 0
            state = (index, added)
            if state in memory:
                return memory[state]
            included = 0
            excluded = 0
            if satisfaction[index] < 0:
                excluded = dp(index + 1, added)
                included = dp(index + 1, added + 1) +  (satisfaction[index] * added)
            else:
                for i in range(index, N):
                    included += satisfaction[i] * added
                    added += 1
            memory[state] = max(included, excluded)
            return memory[state]
        return dp(0, 1)
                    
            
        