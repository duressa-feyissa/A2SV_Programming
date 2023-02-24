class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxDistance = 0
        for trip in trips:
            maxDistance = max(maxDistance, trip[2])
        maxDistance += 1
        
        array = [0] * (maxDistance)
        for passengers, start, end in trips:
            if passengers > capacity:
                return False
            array[start] += passengers
            array[end] -= passengers

        for i in range(1, maxDistance):
            array[i] += array[i - 1]
            if array[i] > capacity:
                return False
        return True
        
        