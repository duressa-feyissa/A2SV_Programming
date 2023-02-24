class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        frequency = [0] * n
        for start, end in requests:
            frequency[start] += 1
            if end + 1 < n:
                frequency[end + 1] -= 1
        
        for i in range(1, n):
            frequency[i] += frequency[i - 1]
        
        indexHash = {}
        for index in range(n):
            indexHash[index] = frequency[index]

        sortedIndex = sorted(indexHash.items(), key=lambda x:x[1])
        left = 0
        cnum = sorted(nums)
        for val in sortedIndex:
            nums[val[0]] = cnum[left]
            left += 1

        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        
        answer = 0
        for start, end in requests:
            if start > 0:  
                answer += nums[end] - nums[start - 1]
            else:
                answer += nums[end]
        
        return answer % (10**9 + 7)
        