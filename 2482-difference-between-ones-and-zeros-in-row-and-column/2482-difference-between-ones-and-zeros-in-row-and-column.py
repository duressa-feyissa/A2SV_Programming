class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        hash_col = {}
        hash_row = {}
        
        for r_index, row in enumerate(grid):
            count_row_one = 0
            for c_index, col in enumerate(row):
                if col == 1:
                    count_row_one+=1
                    hash_col[c_index] = 1 + hash_col.get(c_index, 0)
                else:
                    hash_col[c_index] = 0 + hash_col.get(c_index, 0)
                    
            hash_row[r_index] = count_row_one

        row_length = len(grid)
        col_length = len(grid[0])
        
        for i in range(row_length):
            for j in range(col_length):
                x = hash_row[i] + hash_col[j]
                y = (row_length - hash_row[i]) + (col_length - hash_col[j])         
                grid[i][j] = x - y
        return grid
            
                    
                
                
        