class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        check = Counter(p)
        n = len(p)
        window = Counter(s[:n])
        initial = 1 if window == check else 0
        ans = []
        if initial:
            ans.append(0)
        for i in range(n, len(s)):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
            window[s[i - n]] -= 1
            if window[s[i - n]] == 0:
                del window[s[i - n]]
            if window == check:
                ans.append(i - n + 1)
        return ans
            
            
                
        