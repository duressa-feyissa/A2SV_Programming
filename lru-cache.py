class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.memory = {}

    def move_to_front(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        if key not in self.memory:
            return -1

        node = self.memory[key]
        self.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            node = self.memory[key]
            node.val = value
            self.move_to_front(node)
        else:
            new_node = Node(key, value)
            self.memory[key] = new_node

            if self.capacity == 0:
                del self.memory[self.tail.key]
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            if self.capacity > 0:
                self.capacity -= 1