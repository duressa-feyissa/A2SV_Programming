class StockSpanner:

    def __init__(self):
        self.StockSpanner = []
        self.stack = []
        self.index = 0
    
    def next(self, price: int) -> int:
        anyPop = False
        answer = 0

        while self.stack and self.StockSpanner[self.stack[-1]] <= price:
            anyPop = True
            self.stack.pop()
        
        if self.index == 0 or not anyPop:
            answer = 1
        else:
            if self.stack:
                answer =  self.index - self.stack[-1]
            else:
                answer = self.index + 1
        
        self.StockSpanner.append(price)
        self.stack.append(self.index)
        self.index += 1
        
        return answer
        
        





        



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)