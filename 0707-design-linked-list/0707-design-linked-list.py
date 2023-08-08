class Node:
    def __init__(self, val: int, next_node: Optional['Node'] = None) -> None:
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        count = 0
        node = self.head
        while node and count <= index:
            if count == index:
                return node.val
            node = node.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        
    def addAtTail(self, val: int) -> None:
        node = self.head
        if not node:
            self.head = Node(val)
            return
        while node and node.next:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        prev = None
        count = 0
        if index == 0 and not node:
            self.head = Node(val)
            return
        while node and count <= index:
            if count == index:
                print(count, node.val)
                if count == 0:
                    self.head = Node(val, self.head)
                else:
                    prev.next = Node(val, node)
                return
            prev = node
            node = node.next
            count += 1
        if not node and count == index:
            prev.next = Node(val)

    def deleteAtIndex(self, index: int) -> None:
        prev = None
        node = self.head
        count = 0
        while node and count <= index:
            if count == index:
                if count == 0:
                    self.head = self.head.next
                else:
                    prev.next = node.next
                return
            prev = node
            node = node.next
            count += 1

            
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
