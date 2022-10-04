class MyQueue:

    def __init__(self):
        self.new = []

    def push(self, x: int) -> None:
        self.new.append(x)

    def pop(self) -> int:
        x = self.new[0]
        self.new = self.new[1:]
        return x

    def peek(self) -> int:
        return self.new[0]

    def empty(self) -> bool:
        return not bool(self.new)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
