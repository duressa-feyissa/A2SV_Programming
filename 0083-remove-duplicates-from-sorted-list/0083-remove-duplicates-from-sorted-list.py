# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        while node and node.next:
            temp = node.next
            while temp and node.val == temp.val:
                prev = temp
                temp = temp.next
                del prev
            node.next = temp
            node = node.next
        
        return head
        