class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memory = {}
        N = len(questions)
        def dp(index):
            if index >= N:
                return 0
            if index not in memory:
                memory[index] = max(dp(index + questions[index][1] + 1) + questions[index][0], dp(index + 1))
            return memory[index]
        return dp(0)
    
                    
            
            
        