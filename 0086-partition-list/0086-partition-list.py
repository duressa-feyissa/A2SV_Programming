# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerNumberHead = None
        largeNumberHead = None
        smallNode=None
        largeNode=None
        node = head
        flag1=True
        flag2=True
        while node:
            if node.val < x and flag1:
                smallerNumberHead = node
                smallNode = node
                node = node.next
                smallNode.next = None
                flag1=False
            elif node.val >= x and flag2:
                largeNumberHead = node
                largeNode = node
                node = node.next
                largeNode.next = None
                flag2=False
            elif node.val < x and not flag1:
                smallNode.next = node
                node = node.next
                smallNode = smallNode.next
                smallNode.next = None
            elif node.val >= x and not flag2:
                largeNode.next = node
                node = node.next
                largeNode = largeNode.next
                largeNode.next = None
        if smallNode:
            smallNode.next = largeNumberHead
            return smallerNumberHead
        return largeNumberHead
        
        
        