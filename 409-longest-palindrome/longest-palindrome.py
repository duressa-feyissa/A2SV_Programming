class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        odd_found = False
        
        for count in counts.values():
            length += count if count % 2 == 0 else count - 1
            if count % 2 == 1:
                odd_found = True
                
        return length + 1 if odd_found else length