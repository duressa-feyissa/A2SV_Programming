class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N = len(arr)
        memory = defaultdict(int)
        for i in range(N):
            memory[arr[i]] = memory[arr[i] - difference] + 1
        return max(list(memory.values()))