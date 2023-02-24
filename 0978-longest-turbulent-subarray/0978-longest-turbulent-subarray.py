class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        ans = 1
        n = len(arr)
        if n == 2:
            return int(arr[0] != arr[1]) + 1
        left = 0
        for right in range(2, n):
            curr = arr[right] - arr[right - 1]
            prev = arr[right - 1] - arr[right - 2]
            
            if (curr > 0 and prev < 0) or (curr < 0 and prev > 0):
                ans = max(ans, right - left + 1)
            elif curr == 0:
                left = right
            else:
                ans = max(ans, 2)
                left = right - 1
        
        return ans
            
        
        
                
                
                
            
            
            
            
        