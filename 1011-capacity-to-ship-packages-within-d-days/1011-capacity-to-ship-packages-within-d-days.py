class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = 1
        high = sum(weights)
        valid = 0
        Max = max(weights)
        
        while low <= high:
            
            middle = (low + high) // 2            
            count_days = 0
            add = 0

            for weight in weights:
                add += weight
                if add == middle:
                    count_days += 1
                    add = 0
                elif add > middle:
                    count_days += 1
                    add = weight
            if add > 0:
                count_days += 1

            if count_days <= days:
                if middle  >= Max:
                    high = middle - 1               
                else:
                    low = middle + 1
            else:
                low = middle + 1
        
        return low
                
                
            
            
             
            
            
        
        
        
