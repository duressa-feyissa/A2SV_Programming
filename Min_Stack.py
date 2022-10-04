class MinStack:

    def __init__(self):
        self.new = []
        
    def push(self, val: int) -> None:
        if len(self.new) == 0:
            self.new.append([val, val])
        else:
            self.new.append([val, val if self.new[-1][1] > val else self.new[-1][1]])
    def pop(self) -> None:
        self.new.pop()
        
    def top(self) -> int:
        return self.new[-1][0]

    def getMin(self) -> int:
        return self.new[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
