class Solution:

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        answer = []
        for i in range(king[0]-1,-1,-1):#North
            if [i,king[1]] in queens:
                answer.append([i,king[1]])
                break
        for i in range(king[0]+1,8):#South
            if [i,king[1]] in queens:
                answer.append([i,king[1]])
                break
        for i in range(king[1]+1,8):#East
            if [king[0],i] in queens:
                answer.append([king[0],i])
                break
        for i in range(king[1]-1, -1,-1):#West
            if [king[0],i] in queens:
                answer.append([king[0],i])
                break
        i = king[0] - 1
        j = king[1] - 1 
        while i >= 0 and j >= 0:#NothWest
            if [i,j] in queens:
                answer.append([i,j])
                break
            i-=1
            j-=1
        i = king[0] - 1
        j = king[1] + 1 
        while i >= 0 and j < 8:#NortEast
            if [i,j] in queens:
                answer.append([i,j])
                break
            i-=1
            j+=1
        i = king[0] + 1
        j = king[1] + 1 
        while i < 8 and j < 8:#SouthEast
            if [i,j] in queens:
                answer.append([i,j])
                break
            i+=1
            j+=1
        i = king[0] + 1
        j = king[1] - 1 
        while i < 8 and j >= 0:#SouthWest
            if [i,j] in queens:
                answer.append([i,j])
                break
            i+=1
            j-=1
        return answer
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        
        
        
        