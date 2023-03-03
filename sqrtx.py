class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        prev = -1
        left = 1
        right = x
        middle = 0
        while left <= right:    
            middle = left + (right - left) // 2
            prev = middle
            if (middle * middle) > x:
                right = middle - 1
            elif (middle * middle) < x:
                left = middle + 1
            else:
                break
        if right < left:
            prev = right
        return int(prev)