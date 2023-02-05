# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        digit = 0
        
        while l1 or l2:
            if l1 and l2:
                add = l1.val + l2.val + digit
                node.next = ListNode(add % 10)
                digit = add // 10
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                add = l1.val + digit
                node.next = ListNode(add % 10)
                digit = add // 10
                l1 = l1.next
            elif l2 and not l1:
                add = l2.val + digit
                node.next = ListNode(add % 10)
                digit = add // 10
                l2 = l2.next
            node = node.next
        if digit != 0:
            node.next = ListNode(digit)
        return dummy.next
                
                