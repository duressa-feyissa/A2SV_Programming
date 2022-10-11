# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new = {}
        while node != None:
            if node.val in new:
                new[node.val] += 1
            else:
                new[node.val] = 1
            node = node.next
        node = head
        tmp = ListNode(0,None)
        head = tmp
        while node != None:
            if new[node.val] == 1:
                tmp.next = node
                tmp = tmp.next
            node = node.next
        tmp.next = None
        head = head.next
        return head
                
        
        
