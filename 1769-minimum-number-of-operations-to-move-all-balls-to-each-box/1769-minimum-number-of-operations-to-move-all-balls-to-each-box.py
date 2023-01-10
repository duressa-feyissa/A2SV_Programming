class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        answer = []
        
        for i in range(len(boxes)):
            add = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    add += abs(i - j)
            answer.append(add)
        
        return answer
                    
        
        
        