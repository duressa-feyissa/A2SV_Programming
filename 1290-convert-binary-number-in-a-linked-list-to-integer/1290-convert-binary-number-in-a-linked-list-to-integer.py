# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ""
        node=head
        while node:
            binary += str(node.val)
            node = node.next
        ans = 0
        pow = 0
        n = len(binary)
        for i in range(n):
            ans += ((2 ** i) * int(binary[n - i - 1]))
        
        return ans
        
        
        
        