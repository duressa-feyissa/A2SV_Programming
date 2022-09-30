class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new = [0 for i in range(len(points))]
        j = 0
        for i in points:
            new[j] = (i[0] * i[0]) + (i[1] * i[1])
            j += 1
        tmp = new.copy()
        tmp.sort()
        hold = []
        for i in range(k):
            index = new.index(tmp[i])
            new[index] = -1
            hold.append(points[index])
        return hold
