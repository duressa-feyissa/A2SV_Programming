class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        left = right = 0
        ans = m + 1
        index = [0,0]
        target = Counter(t)
        window = defaultdict(int)
        windowLength = 0
        targetLength = len(target)
        
        for right in range(m):
            if s[right] in target:
                window[s[right]] += 1
            
            if s[right] in target and window[s[right]] == target[s[right]]:
                windowLength += 1
            
            if windowLength == targetLength:
                while left <= right:
                    if windowLength == targetLength:
                        if right - left + 1 < ans:
                            ans = right - left + 1
                            index = [left, right]
                    if s[left] in target:
                        if windowLength == targetLength:
                            window[s[left]] -= 1
                            if window[s[left]] == 0:
                                window.pop(s[left])
                            if window[s[left]] < target[s[left]]:
                                windowLength -= 1
                            left += 1
                        else:
                            break
                    else:
                        left += 1
        
        return "" if ans == m + 1 else s[index[0]: index[1]+1]
            
            
        
                
            
            
            
            
        
        
        
        
                
            
                
                
                
                
            
            
        
        
        
        
        
        