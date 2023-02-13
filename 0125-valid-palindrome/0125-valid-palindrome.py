class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalnum():
                result += i
        
        res = result.lower()
        
        return res == res[::-1]
        