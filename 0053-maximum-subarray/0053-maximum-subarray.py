class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0]
        for i in range(N):
            prefix.append(prefix[-1] + nums[i])
        queue = deque([])
        largestSum = float('-inf')
        for i in range(N):
            if queue:
                largestSum = max(largestSum, prefix[queue[-1] + 1] - prefix[queue[0]])
            while queue and prefix[queue[-1] + 1] - prefix[queue[0]] < 0:
                queue.popleft()
            queue.append(i)
        if queue:
            largestSum = max(largestSum, prefix[queue[-1] + 1] - prefix[queue[0]])
        return largestSum