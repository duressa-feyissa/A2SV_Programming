class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = str(x)
        z = str(x)[::-1]
        if y == z:
            return True
        else:
            return False
        