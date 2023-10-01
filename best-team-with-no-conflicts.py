class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        array = []
        for i in range(N):
            array.append((ages[i], scores[i]))
        array.sort()
        dp = []
        for i in range(N):
            dp.append(array[i][1])
        for i in range(1, N):
            for j in range(i):
                if array[j][1] <= array[i][1]:
                    dp[i] = max(dp[i], dp[j] + array[i][1])
        
        return max(dp)