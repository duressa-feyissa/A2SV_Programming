# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        array = []
        N = len(lists)
        for i in range(N):
            if lists[i]:
                heappush(array, (lists[i].val, i))

        while array:
            _, index = heappop(array)
            node.next = lists[index]
            lists[index] = lists[index].next
            node = node.next
            if lists[index]:
                heappush(array, (lists[index].val, index))
        node.next = None
        return dummy.next