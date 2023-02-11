# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        add = 0
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = prev
            prev = temp
        
        while slow:
            add = max(slow.val + prev.val, add)
            slow = slow.next
            prev = prev.next
        
        return add
            
        