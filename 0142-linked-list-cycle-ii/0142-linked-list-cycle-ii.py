# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        else:
            return None
        
        left = head
        while left:
            if fast is left:
                return fast
            left = left.next
            fast = fast.next
        
        
        
        