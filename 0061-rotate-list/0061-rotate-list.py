# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        n = 1
        node = head
        while node.next:
            node = node.next
            n += 1
        prevtail = node
        
        k = k % n
        if k == 0:
            return head
        
        node = head
        prev = None
        
        left = 0
        while left < n - k:
            prev = node
            node = node.next
            left += 1
            
        prevtail.next = head
        prev.next = None
        return  node
        
        
        
        
            
        

        