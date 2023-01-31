# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        ptr = head
        head = head.next
        ptr.next = None
        while head:      
            temp = head
            head = head.next
            temp.next = ptr
            ptr = temp
        return ptr
    
        
            