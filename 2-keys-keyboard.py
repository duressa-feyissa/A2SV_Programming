class Solution:
    def minSteps(self, n: int) -> int:
        memory = [-1] * (n + 1)
        for i in range(1,n+1):
            found = False
            for j in range(i-1, 0,-1):
                if memory[j] != -1 and i % j == 0:
                    memory[i]= (i // j) + memory[j]
                    found = True
                    break
            if not found:
                memory[i] = i
        return memory[n] - 1