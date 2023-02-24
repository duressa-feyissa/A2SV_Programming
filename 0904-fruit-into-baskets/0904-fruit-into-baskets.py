class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        counter = defaultdict(int)
        left = 0
        answer = 0
        baskets = 0
        
        for right in range(n):
            counter[fruits[right]] += 1
            
            if counter[fruits[right]] == 1:
                baskets += 1
                
            if baskets <= 2:
                answer = max(answer, right - left + 1)

            while baskets > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    baskets -= 1
                left += 1
        return answer
            
            
            
                
            
            
        
        