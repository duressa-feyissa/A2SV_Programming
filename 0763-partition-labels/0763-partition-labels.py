class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frequency = Counter(s)
        left = 0
        right = 0
        n = len(s)
        check = set()
        answer = []
        while left < n:
            start = left
            while right < n and (frequency[s[start]] > 0 or check):
                if s[right] not in check:
                    check.add(s[right])
                frequency[s[right]] -= 1
                if frequency[s[right]] == 0 and s[start] != s[right]:
                    check.discard(s[right])
                if len(check) == 1 and frequency[s[start]] == 0:
                    break
                right += 1
            answer.append(right - left + 1)
            check.clear()
            right += 1
            left = right
        return answer
            
                
            
            
            
            
            
            
        
        