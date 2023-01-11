class Solution:

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        hash_map = {
            "N":[-1,-1], "NE":[-1,-1], "NW":[-1,-1], "S":[-1,-1],
            "E":[-1,-1], "W":[-1,-1], "SE":[-1,-1], "SW":[-1,-1]
        }
        for queen in queens:
            #North 
            if queen[0] - king[0] < 0 and queen[1] - king[1] == 0:
                if hash_map["N"] == [-1,-1]:
                    hash_map['N'] = queen
                else:
                    if self.direction_check(king, queen, "N", hash_map):
                        hash_map['N'] = queen                        
            #South
            elif queen[0] - king[0] > 0 and queen[1] - king[1] == 0:
                if hash_map["S"] == [-1,-1]:
                    hash_map['S'] = queen
                else:
                    if self.direction_check(king, queen, "S", hash_map):
                        hash_map['S'] = queen 
            #East
            elif queen[0] - king[0] == 0 and queen[1] - king[1] > 0:
                if hash_map["E"] == [-1,-1]:
                    hash_map['E'] = queen
                else:
                    if self.direction_check(king, queen, "E", hash_map):
                        hash_map['E'] = queen 
            #West
            elif queen[0] - king[0] == 0 and queen[1] - king[1] < 0:
                if hash_map["W"] == [-1,-1]:
                    hash_map['W'] = queen
                else:
                    if self.direction_check(king, queen, "W", hash_map):
                        hash_map['W'] = queen 
            #NothWest
            elif queen[0] - king[0] < 0 and queen[1] - king[1] < 0 and self.diagonal_check(king, queen):
                if hash_map["NW"] == [-1,-1]:
                    hash_map['NW'] = queen
                else:
                    if self.direction_check(king, queen, "NW", hash_map):
                        hash_map['NW'] = queen 
            #NorthEast
            elif queen[0] - king[0] < 0 and queen[1] - king[1] > 0 and self.diagonal_check(king, queen):
                if hash_map["NE"] == [-1,-1]:
                    hash_map['NE'] = queen
                else:
                    if self.direction_check(king, queen, "NE", hash_map):
                        hash_map['NE'] = queen 
            #SouthEast
            elif queen[0] - king[0] > 0 and queen[1] - king[1] > 0 and self.diagonal_check(king, queen):
                if hash_map["SE"] == [-1,-1]:
                    hash_map['SE'] = queen
                else:
                    if self.direction_check(king, queen, "SE", hash_map):
                        hash_map['SE'] = queen 
            #SouthWest
            elif queen[0] - king[0] > 0 and queen[1] - king[1] < 0 and self.diagonal_check(king, queen):
                if hash_map["SW"] == [-1,-1]:
                    hash_map['SW'] = queen
                else:
                    if self.direction_check(king, queen, "SW", hash_map):
                        hash_map['SW'] = queen
        answer = []
        for value in hash_map.values():
            if value != [-1,-1]:
                answer.append(value)
        return answer

    def direction_check(self, king, queen, direction, hash_map):
        distance1 = abs(queen[0] - king[0]) + abs(queen[1] - king[1])
        distance2 = abs(hash_map[direction][0] - king[0]) + abs(hash_map[direction][1] - king[1])
        if distance1 < distance2:
            return 1
        return 0
    def diagonal_check(self, king, queen):
        if abs(king[0]-queen[0]) == abs(king[1] - queen[1]):
            return 1
        return 0
        
        