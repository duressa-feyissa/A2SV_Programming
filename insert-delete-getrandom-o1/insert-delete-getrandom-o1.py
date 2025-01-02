class RandomizedSet:

    def __init__(self):
        self.hashTable = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.hashTable:
            self.hashTable[val] = len(self.array)
            self.array.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashTable:
            self.hashTable[self.array[-1]] = self.hashTable[val]
            self.array[self.hashTable[val]] = self.array[-1]
            self.array.pop()
            self.hashTable.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()