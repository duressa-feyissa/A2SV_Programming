class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        initial_satisfaction = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        max_additional_satisfaction = 0
        current_additional_satisfaction = 0
        
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
        
        max_additional_satisfaction = current_additional_satisfaction
        
        for i in range(minutes, n):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                current_additional_satisfaction -= customers[i - minutes]
            
            max_additional_satisfaction = max(max_additional_satisfaction, current_additional_satisfaction)
        
        return initial_satisfaction + max_additional_satisfaction
