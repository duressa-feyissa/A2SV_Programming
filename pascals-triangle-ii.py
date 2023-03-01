class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = self.getRow(rowIndex - 1)
        temp = []
        for i in range(1, len(result)):
            temp.append(result[i] + result[i- 1])
        return [1] + temp + [1]