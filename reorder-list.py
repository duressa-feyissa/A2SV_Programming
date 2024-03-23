# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        array = []
        node = head
        while node:
            array.append(node)
            node = node.next
        left, right = 0, len(array) - 1
        N = len(array)
        while left < (N // 2 + (N % 2)) and N != 1:
            array[left].next = array[right]
            array[right].next = array[left + 1]
            left += 1
            right -= 1
        if N % 2 == 0:
            array[N // 2 + (N % 2)].next = None
        else:
            array[N//2].next = None