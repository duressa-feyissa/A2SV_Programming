class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        tmp = []
        tmp.append(intervals[0].copy())
        for i in intervals:
            n = len(tmp) - 1
            if tmp[n][1] >= i[0] and tmp[n][1] < i[1]:
                tmp[n][1] = i[1]
            if tmp[n][1] < i[0] and tmp[n][1] < i[1]:
                tmp.append(i)
        return tmp
                
        
