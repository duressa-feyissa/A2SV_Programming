# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        DICT = {head.val: head}
        Node = head
        tmp = head
        while Node:
            if Node.val in DICT:
                pass
            else:
                DICT[Node.val] = Node
                tmp.next = Node
                tmp = tmp.next
            Node = Node.next
        tmp.next = None
        return head 
