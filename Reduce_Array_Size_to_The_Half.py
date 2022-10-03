class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        new = {}
        for i in range(len(arr)):
            if arr[i] in new:
                new[arr[i]] += 1
            else:
                new[arr[i]] = 1
        sorted_order = sorted(new.items(), key=lambda x:x[1], reverse=True)
        count = 0
        j = 0
        for i in sorted_order:
            if count >= len(arr) // 2:
                break
            count += i[1]
            j += 1
        return j
            
