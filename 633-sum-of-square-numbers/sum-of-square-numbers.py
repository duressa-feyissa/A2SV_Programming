class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            add = left ** 2 + right ** 2
            if add == c:
                return True
            elif add < c:
                left += 1
            else:
                right -= 1
        return False
                
                
        