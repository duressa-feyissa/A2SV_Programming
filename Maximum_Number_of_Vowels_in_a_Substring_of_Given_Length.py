class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        Max, result = 0, 0
        for i in range(k):
            if s[i] in vowels:
                result+=1
        Max = max(Max,result)
        for i in range(k,len(s)):
            if s[i] in vowels:
                if s[i-k] in vowels:
                    pass
                else:
                    result += 1
            else:
                if s[i-k] in vowels:
                    result -= 1
            Max = max(Max,result)
        return Max
                    
                    
                
                
            
            
            
        
