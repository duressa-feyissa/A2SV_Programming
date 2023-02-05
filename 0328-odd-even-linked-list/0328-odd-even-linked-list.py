# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenDummy = ListNode()
        oddDummy = ListNode()
        even = evenDummy
        odd = oddDummy
        node = head
        
        i = 0
        while node:
            if i % 2:
                even.next = node
                even = even.next
                node = node.next
                even.next= None
            else:
                odd.next = node
                odd = odd.next
                node = node.next
                odd.next= None
            i += 1
        
        odd.next = evenDummy.next
        return oddDummy.next
        
        
        
        
            
        
        