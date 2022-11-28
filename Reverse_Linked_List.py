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
            hold.append(Node.val)
            Node = Node.next
        hold.reverse()
        head = ListNode()
        Node = head
        i = 0
        while i < len(hold):
            if i == len(hold) - 1:
                Node.val = hold[i]
            else:
                Node.val = hold[i]
                Node.next = ListNode()
            i+=1
            Node = Node.next
        return head

