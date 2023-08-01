class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memory = [0] * (query_row + 2)
        memory[0] = poured
        for i in range(1,query_row + 1):
            next = [0] * (query_row + 2)
            for j in range(i + 1):
                if memory[j] > 1:
                    half = (memory[j] - 1) / 2
                    next[j] += half
                    next[j+1] += half
            memory = next
        if memory[query_glass] >= 1:
            return 1.0
        return memory[query_glass]


    
        
                
                
                
    