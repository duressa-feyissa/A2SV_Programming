class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        right = [0,0]
        down = [0,n - 1]
        up = [m-1,0]
        left = [m-1,n-1]
        
        while True: 
            if n % 2 != 0:
                if right[1] == down[1]:
                    break
            else:
                if left[0] + 1 == right[1]:
                    break
            while right[1] < down[1]:
                tmp1 = matrix[right[0]][right[1]]
                tmp2 = matrix[down[0]][down[1]]
                matrix[right[0]][right[1]] = matrix[up[0]][up[1]]
                matrix[down[0]][down[1]] = tmp1
                matrix[up[0]][up[1]] = matrix[left[0]][left[1]]
                matrix[left[0]][left[1]] = tmp2
                right[1] += 1
                down[0] += 1
                left[1] -= 1
                up[0] -= 1
            right[0] += 1
            right[1] = right[0]
            down[0] = right[0]
            down[1] -= 1
            left[1] = down[1]
            left[0] -= 1
            up[1] = right[1]
            up[0] = left[0]

        
            
        