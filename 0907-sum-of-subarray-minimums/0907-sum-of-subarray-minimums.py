class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        minToRight = [0] * n
        minToLeft = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                popped = stack.pop()
                minToRight[popped] = i - popped
            stack.append(i)
        
        while stack:
            popped = stack.pop()
            minToRight[popped] = n - popped
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                popped = stack.pop()
                minToLeft[popped] = popped - i
            stack.append(i)
        
        while stack:
            popped = stack.pop()
            minToLeft[popped] = popped - (-1)

        ans = 0
        for i in range(n):
            ans += ((minToLeft[i] * minToRight[i]) * arr[i])
        
        return ans % (10**9 + 7)


