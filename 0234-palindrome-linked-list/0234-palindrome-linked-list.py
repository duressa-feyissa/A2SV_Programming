# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        res = False
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        if fast is None:
             res = Solution.check(slow, head, count)
        else:
             res = Solution.check(slow.next, head, count)
        return res
    
    @staticmethod
    def check(right, head, count):
        node = head
        reverse = None
        i = 0
        while i < count:
            temp = node
            node = node.next
            temp.next = reverse
            reverse = temp
            i+=1
        while right:
            if right.val != reverse.val:
                return False
            right = right.next
            reverse = reverse.next
        return True