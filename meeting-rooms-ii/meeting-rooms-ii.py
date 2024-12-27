class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        MIN, MAX = float('inf'), float('-inf')
        for x, y in intervals:
            MIN = min(MIN, x)
            MAX = max(MAX, y)
        
        array = [0] * (MAX - MIN + 2)
        
        for i in range(len(intervals)):
            x, y = intervals[i]
            array[x-MIN] += 1
            array[y-MIN] -= 1
        
        for i in range(1, len(array)):
            array[i] += array[i-1]
        
        return max(array)
            
        