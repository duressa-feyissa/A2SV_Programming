class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxDistance = 0
        for trip in trips:
            maxDistance = max(maxDistance, trip[2])
        
        maxDistance += 1
        
        array = [0] * (maxDistance)
        for trip in trips:
            if trip[0] > capacity:
                return False
            array[trip[1]] += trip[0]
            array[trip[2]] -= trip[0]

        for i in range(1, maxDistance):
            array[i] += array[i - 1]
            if array[i] > capacity:
                return False
        return True
        
        