class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        array = []
        for i in range(len(points)):
            cal = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1])
            array.append([cal, i])
        array.sort()
        print(array)
        ans = []
        for i in range(k):
            ans.append(points[array[i][1]])
        return ans
            