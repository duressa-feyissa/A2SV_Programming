class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    
        dictionary = defaultdict(list)
        
        for index, point in enumerate(points):
            if x == point[0] or y == point[1]:
                distance = abs(point[0] - x) + abs(point[1] - y)
                dictionary[distance].append(index)
        
        if (len(dictionary.keys()) == 0):
            return -1
        
        min_distance = min(dictionary.keys())
        return dictionary[min_distance][0]
        
        
        
        