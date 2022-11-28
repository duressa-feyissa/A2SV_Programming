# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = [], []
        while l1:
            list1.append(l1.val)
            l1 = l1.next

        while l2:
            list2.append(l2.val)
            l2 = l2.next

        num = len(list1) if len(list1) >= len(list2) else len(list2)
        i = 0
        r = 0
        new_node = ListNode()
        head = new_node
        while i < num:
            add = 0
            if i < len(list1):
                add += list1[i]
            if i < len(list2):
                add += list2[i] 
            tmp = (add + r) % 10 
            r = (add + r) // 10
            new_node.val = tmp
            if i + 1 < num:
                new_node.next = ListNode()
            if r != 0 and i == num - 1:
                new_node.next = ListNode(r, None)
                break
            new_node = new_node.next
            i+=1
        return head
