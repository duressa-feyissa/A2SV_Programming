class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = self.reverse_string(str(num)).lstrip('0')
        reversed2 = self.reverse_string(reversed1).lstrip('0')
        return str(num).lstrip('0') == reversed2

    def reverse_string(self, s):
        return s[::-1]