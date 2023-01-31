# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        data = []
        while node:
            data.append(node.val)
            node = node.next
        reverse = data.copy()
        reverse.reverse()
        if data == reverse:
            return True
        return False