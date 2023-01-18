class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        transpose = list(zip(*board))
        for row in range(9):
            #check row
            dot = board[row].count(".")
            num = len(set(board[row]))
            if num - 1 + dot != 9:
                return False           
            
            #check colums
            dot = transpose[row].count(".")
            num = len(set(transpose[row]))
            if num - 1 + dot != 9:
                return False
        
        top = 0
        left = 0
        while top <= len(board) - 3:
            while left <= len(board[0]) - 3:
                if not Solution.checkCell(self,board, top, left):
                    return False
                left += 3
            top += 3
            left = 0
        return True

    def checkCell(self, board, top, left)->bool:
        temp = []
        for i in range(top, top+3):
            for j in range(left, left+3):
                if board[i][j] != ".":
                    temp.append(board[i][j])
        if len(temp) == len(set(temp)):
            return True
        return False