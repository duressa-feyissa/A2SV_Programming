class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        left1 = 0
        left2 = 0
        m = len(players)
        n= len(trainers)
        result = 0
        while left1 < m and left2 < n:
            if players[left1] <= trainers[left2]:
                result += 1
                left1 += 1
                left2 += 1
            else:
                while left2 < n and players[left1] > trainers[left2]:
                    left2 += 1
        return result
        
        