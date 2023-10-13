class MinStack:

    def __init__(self):
        self.stack = []   
        self.minimum = []

    def push(self, val: int) -> None:
        if self.stack:
            if self.minimum[-1] >= val:
                self.minimum.append(val)
        else:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack and self.stack[-1] == self.minimum[-1]:
            self.minimum.pop()
            self.stack.pop()
        elif self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()