class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        array = []
        for i in range(N):
            array.append((ages[i], scores[i]))
        array.sort()
        array = [(0, 0)] + array
        # memory = {}
        # def dp(index, maxIndex):
        #     if index > N:
        #         return 0
        #     state = (index, maxIndex)
        #     if state in memory:
        #         return memory[state]
        #     include = 0
        #     exclude = dp(index + 1, maxIndex)
        #     if array[index][1] >= array[maxIndex][1]:
        #         include = dp(index + 1, index) + array[index][1]
        #     memory[state] = max(include, exclude)
        #     return memory[state]
        # return dp(0, 0)
    
        
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            for j in range(i):
                if array[j][1] <= array[i][1]:
                    dp[i] = max(dp[i], dp[j] + array[i][1])
        
        return max(dp)
            
        



            

        