class DataStream:

    def __init__(self, value: int, k: int):
        self._deque = deque()
        self.value = value
        self.k = k
        self.size = 0
        self.counter = defaultdict(int)

    def consec(self, num: int) -> bool:
        if self.size == self.k:
            x = self._deque.popleft()
            self.size -= 1
            self.counter[x] -= 1            
        
        self.counter[num] += 1
        self._deque.append(num)   
        self.size += 1
        
        if self.size < self.k:
            return False
        return self.counter[self.value] == self.k
    
            
            

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)