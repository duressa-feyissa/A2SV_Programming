class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = -1
        self.rear = -1
        self.size = 0
        self.maxSize = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False        
        else:
            self.rear += 1
            if self.rear == self.maxSize:
                self.rear = 0
            self.queue[self.rear] = value
            self.size += 1
            if self.front == -1:
                self.front += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.front += 1
        if self.front == self.maxSize:
            self.front = 0
        return True
            
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.size != 0:
            return False
        return True

    def isFull(self) -> bool:
        if self.size == self.maxSize:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()