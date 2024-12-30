class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        reversed_x = int(str(x)[::-1])
        
        if is_negative:
            reversed_x = -reversed_x
        
        if -(2**31) <= reversed_x <= 2**31 - 1:
            return reversed_x
        return 0
