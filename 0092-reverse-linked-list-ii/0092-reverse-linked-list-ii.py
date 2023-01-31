# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #Finding node before left and node at right
        nodeBeforeLeft = None
        nodeAtRight = None
        node = head
        prev = None
        i = 1
        while i <= right:
            if i == left:
                nodeBeforeLeft = prev
            if i == right:
                nodeAtRight = node
            prev = node
            node = node.next
            i += 1
        
        #Reverse
        if nodeBeforeLeft:
            node = nodeBeforeLeft.next
        else:
            node = head
        reverse = nodeAtRight.next
        i = left
        while i <= right:
            temp = node
            node = node.next
            temp.next = reverse
            reverse = temp
            i += 1
        
        #join
        if nodeBeforeLeft:
            nodeBeforeLeft.next = reverse
        else:
            head = reverse
        return head
        
        
        
        
            
            
        
    
        
        
        
        
        
            
        
        