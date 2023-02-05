# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        left = head
        right = head
        while left:
            count = 0
            while right and left.val == right.val:
                count += 1
                right = right.next
            if count == 1:
                node.next = left
                node = node.next
                left = right
                node.next = None
            else:
                left = right
        return dummy.next
                

            
            
        