class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_lists = [node for node in lists if node]
        lists = new_lists
        
        N = len(lists)
        if N == 0:
            return None
        
        array = []
        for node in lists:
            current = node
            while current:
                array.append(current.val)
                current = current.next
        
        array.sort()
        
        dummy = ListNode(0)
        current = dummy
        for value in array:
            current.next = ListNode(value)
            current = current.next
        
        return dummy.next