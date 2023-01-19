class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        answer = []
        temp = []
        for index in range(len(original)):
            temp.append(original[index])
            if (index + 1) % n == 0:
                answer.append(temp)
                temp = []
        return answer
                
        