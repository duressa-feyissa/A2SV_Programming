# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None

        if (list1 and list2 and list1.val <= list2.val) or (list1 and not list2):
            node = self.mergeTwoLists(list1.next, list2)
            list1.next = node
            return list1
        elif list1 and list2 and list1.val > list2.val or (list2 and not list1):
            node = self.mergeTwoLists(list1, list2.next)
            list2.next = node
            return list2
        

        
        


        
        



        
            
        
                
        
        