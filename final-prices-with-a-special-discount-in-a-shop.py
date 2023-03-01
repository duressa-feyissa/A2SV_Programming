class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)
        discount = [0] * n
        stack = []
        
        for index, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                popped = stack.pop()
                discount[popped] = price
            stack.append(index)

        final = []
        for i in range(n):
            final.append(prices[i] - discount[i])
        
        return final