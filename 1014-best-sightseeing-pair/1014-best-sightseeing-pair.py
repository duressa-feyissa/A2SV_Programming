class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)
        memory = {}
        def dp(index, stat):
            left, right = 0, 0
            if index > N - 1:
                return float('-inf')
            state = (index, stat)
            if state in memory:
                return memory[state]
            if stat == 1:
                left = dp(index + 1, stat) 
                right = dp(index + 1, stat ^ 1)
                if right != float('-inf'):
                    right = right + values[index] + index 
            else:
                left = dp(index + 1, stat)
                right = values[index] - index
            memory[state] = max(left, right)
            return memory[state]
        return max(dp(0, 1), values[0] +  max(dp(1, 0), values[1] - 1)) 