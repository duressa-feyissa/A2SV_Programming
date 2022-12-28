class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = {}
        losers = {}
        
        for match in matches:
            if match[0] in winners:
                winners[match[0]] += 1
            else:
                winners[match[0]] = 1
          
        for match in matches:
            if match[1] in losers:
                losers[match[1]] += 1
            else:
                losers[match[1]] = 1
            
        answer1 = []
        for winner in winners:
            if winner in losers:
                pass
            else:
                answer1.append(winner)
        
        answer2 = []
        for loser in losers:
            if losers[loser] == 1:
                answer2.append(loser)
        
        answer1.sort()
        answer2.sort()
        return [answer1, answer2]
                
            
            
        