# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        left = head
        temp = None
        shift = False
        
        while left:
            if left.next and left.val <= left.next.val:
                left = left.next
            elif left.next and not left.next.next and left.val > left.next.val:
                temp = left.next
                left.next = None
                left = left.next
                shift = True
            else:
                if not left.next:
                    left = left.next
                else:
                    temp = left.next
                    left.next = left.next.next
                    shift = True
                
            if shift:
                if temp.val < head.val:
                    temp.next = head
                    head = temp
                else:
                    node = head
                    while node.next.val < temp.val:
                        node = node.next
                    temp.next = node.next
                    node.next = temp
                shift = False
                
        return head
                
                
                
                
                
            
            
        
        
        
        