# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0, None)
        large = ListNode(0, None)
        node = head
        smallHead = small
        largeHead = large
        while node:
            if node.val < x:
                small.next = node
                small = small.next
            else:
                large.next = node
                large = large.next
            node = node.next
        large.next = None
        small.next = largeHead.next
        
        return smallHead.next
        
        
        
        
        
        