# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        hold = []
        Node = head
        while Node:
            hold.append(Node)
            Node = Node.next
        hold.reverse()
        i = 0
        while i < len(hold):
            if i == len(hold) - 1:
                hold[i].next = None 
            else:
                hold[i].next = hold[i + 1]
            i+=1
        head = hold[0]
        return head
