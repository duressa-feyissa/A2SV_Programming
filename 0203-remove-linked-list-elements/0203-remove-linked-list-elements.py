# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        left = dummy
        node = head
        while node:
            if node.val != val:
                left.next = node
                node = node.next
                left = left.next
            else:
                node = node.next
        left.next = None
        return dummy.next
        