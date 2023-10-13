class MyHashMap:

    def __init__(self):
        self.memory = {}
        

    def put(self, key: int, value: int) -> None:
        self.memory[key] = value
        

    def get(self, key: int) -> int:
        if key in self.memory:
            return self.memory[key]
        return -1
        
    def remove(self, key: int) -> None:
        if key in self.memory:
            del self.memory[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)