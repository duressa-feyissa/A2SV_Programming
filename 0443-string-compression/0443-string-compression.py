class Solution:
    def compress(self, chars: List[str]) -> int:
        
        result = 0
        left = 0
        n = len(chars)
        k = 0
        while left < n:
            right = left + 1
            if right < n and  chars[left] == chars[right]:
                while right < n and chars[left] == chars[right]:
                    right += 1
                count = right - left + 1
                if count > 9:
                    temp = str(count - 1)
                    result += len(temp) + 1
                    chars[k] = chars[left]
                    for i in range(len(temp)):
                        chars[k + i + 1] = temp[i]
                    k += len(temp) + 1
                else:
                    result += 2
                    chars[k] = chars[left]
                    chars[k + 1] = str(count - 1)
                    k += 2
                left = right
            else:
                chars[k] = chars[left]
                k += 1
                result += 1
                left += 1    
                    
        return result if n > 1 else 1
        
        