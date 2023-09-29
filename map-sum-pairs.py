class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.value = None

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        current = self.root
        for c in key:
            index = ord(c) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index] 
        current.value = val
    def helper(self, pointer):
        count = 0
        for child in pointer.children:
            if child:
                count += self.helper(child)
                if child.value:
                    count += child.value
        return count

    def sum(self, prefix: str) -> int:
        total = 0
        current = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not current.children[index]:
                return total
            if current.value:
                total += current.value
            current = current.children[index]
        if current.value:
            total += current.value
        return total + self.helper(current)

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)