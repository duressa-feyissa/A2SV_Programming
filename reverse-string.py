class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.reverse(s, 0, len(s) - 1)

    def reverse(self, s, left, right):
        if left >= right :
            return
        
        self.reverse(s, left + 1, right - 1)
        s[left], s[right] = s[right], s[left]