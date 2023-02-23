class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = ans = 0
        counter = defaultdict(int)
        cmax = 0
        for right, char in enumerate(s):
            counter[char] += 1
            cmax = max(cmax, counter[char])

            while (right - left - cmax + 1) > k:
                counter[s[left]] -= 1
                left += 1

            ans = max(ans, right - left +1)

        return ans
                    
        
                    
                
                
                
            
        
                
                
                
                
            
                
        