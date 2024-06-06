class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total_sum = 0
        
        for digit in str(n):
            digit = int(digit)
            product *= digit
            total_sum += digit
        
        return product - total_sum