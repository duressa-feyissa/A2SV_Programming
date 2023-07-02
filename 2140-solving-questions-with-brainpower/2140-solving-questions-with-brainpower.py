class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        Max = max(list(map(lambda x: x[1], questions)))
        memory = [0] * (Max + 10 + N)
        for i in range(N - 1, -1, -1):
            memory[i] = max(memory[i + questions[i][1] + 1] + questions[i][0], memory[i + 1])
        return memory[0]
