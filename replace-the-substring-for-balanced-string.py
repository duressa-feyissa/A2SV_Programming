class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        balance = len(s) // 4

        check = defaultdict(int)
        n = len(s)
        
        for c in s:
            if counter[c] > balance:
                counter[c] -= 1
                check[c] += 1
    
        Checklength = len(check)
        if Checklength == 0:
            return 0
        
        window = defaultdict(int)
        left = 0
        formed = 0
        answer = float("inf")
        
        for right in range(n):
            
            if s[right] in check:
                window[s[right]] += 1
            
                if window[s[right]] == check[s[right]]:
                    formed += 1
            
            while left < n and formed == Checklength:
                
                answer = min(answer, right - left + 1)
                
                if s[left] in window:
                    window[s[left]] -= 1
                    
                    if window[s[left]] < check[s[left]]:
                        formed -= 1
                
                left += 1
        
        return answer