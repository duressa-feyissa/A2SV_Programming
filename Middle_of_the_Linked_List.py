# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        i = 0
        while node != None:
            i+=1
            node = node.next
        num = (i // 2) + 1
        i = 0
        node = head
        while i < num - 1:
            i+=1
            node = node.next
        return node
