class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        valid = float('inf')
        middle = 0
        while left <= right:
            
            middle = (left + right) // 2
            
            time = 0
            for num in piles:
                time += ceil(num/middle)

            if time <= h:
                valid = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return valid
                
                
            
            
             
            
            
        
        
        
