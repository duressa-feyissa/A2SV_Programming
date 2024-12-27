class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        return len(heap)
