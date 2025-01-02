class Node:
    def __init__(self, key, val, nextNode=None, prevNode=None):
        self.key = key
        self.val = val
        self.next = nextNode
        self.prev = prevNode

class LRUCache:
    def __init__(self, capacity: int):
        self.N = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def changePosition(self, key):
        if len(self.map) < 2:
            return
        currentNode = self.map[key]
        if currentNode == self.head:
            return
        if currentNode == self.tail:
            self.tail = currentNode.prev
            self.tail.next = None
        else:
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
        currentNode.prev = None
        currentNode.next = self.head
        self.head.prev = currentNode
        self.head = currentNode

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.changePosition(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.changePosition(key)
        else:
            if len(self.map) == self.N:
                del self.map[self.tail.key]
                if self.tail.prev:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    self.head = None
                    self.tail = None
            newNode = Node(key, value)
            if not self.head:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            self.map[key] = newNode
