class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = [i for i in range(1,n+1)]
        left = k - 1
        length = len(array)
        while  length != 1:
            if left < length:                
                array.pop(left)
                left += k - 1
            length = len(array)
            if left >= length:
                left = (left) % length
        return array[0]
                     
"""
#method 2: without removing losers from array
#Ineffective method
        if n == 1:
            return n
        lose = 0
        gap = 0
        while lose != n - 1:
            left = 0
            while left < n and lose != n - 1:
                if left < n and array[left] != -1:
                    gap += 1
                if gap == k:
                    array[left] = -1
                    gap = 0
                    lose += 1
                left += 1
        answer = set(array)
        answer.remove(-1)
        answer = list(answer)[0]
        return answer
"""
        
        
        
        
        
                
                    
                
        
