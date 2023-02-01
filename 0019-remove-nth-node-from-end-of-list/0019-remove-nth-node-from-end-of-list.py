# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count number of node
        node = head
        count = 1
        prev = None
        while node.next:
            prev = node
            node = node.next;
            count+=1
        
        #if count and n == 1
        if count == 1 and n == 1:
            del head
            return None
        
        #if node deleted at the end
        if n == 1:
            prev.next = None
            del node
            return head
        
        #if node deleted at the beginning
        if n == count:
            temp = head
            head = head.next
            del temp
            return head
                    
        #find preview before node deleted
        left = 1
        node = head
        while left < count - n:
            node = node.next
            left += 1
        temp = node.next
        node.next = node.next.next;
        del temp
        
        return head
        
                
        
        
        
        
        
        
            