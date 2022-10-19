class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res, j, add = 0, 0, 0
        for i in range(len(arr)):
            if j == k:
                if add / k >= threshold:
                    res+=1
                add -= arr[i-k]
                j-=1
            if j < k:
                add+=arr[i]
            j+=1
            if j == k and i == len(arr) - 1:
                if add / k >= threshold:
                    res+=1
        return res
        
