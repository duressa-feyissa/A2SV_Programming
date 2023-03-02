class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.solve(x, n)
        return 1 / (self.solve(x, n * -1))
    
    def solve(self, x, n):    
        if n == 0:
            return 1
        if n == 1:
            return x
        
        if n % 2:
            res = (self.solve(x, n // 2) ** 2) * x
            if (res > 2 ** 31 - 1)  or (res < (-2) ** 31):
                return 2 ** 31 - 1
            return res
        else:
            res = self.solve(x, n // 2) ** 2
            if (res > 2 ** 31 - 1)  or (res < (-2) ** 31):
                return 2 ** 31 - 1
            return res
