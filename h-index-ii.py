class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        
        
        while left <= right:
            middle = (left + right) // 2
            if citations[middle] >= (n - middle):
                right = middle - 1
            else:
                left = middle + 1
            
        return n - left