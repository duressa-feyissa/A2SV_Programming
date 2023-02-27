class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        queue = deque ()
        done = True
        
        for ticket in tickets:
            queue.append([ticket, 0])
        
        queue[k][1] = "#"
        count = 0

        while done:
            popped = queue.popleft()
            if popped[0] != 1:
                popped[0] -= 1
                queue.append(popped)
            elif popped[1] == "#":
                done = False
            count += 1
            
        return count
                
        
                
        
        
            
        