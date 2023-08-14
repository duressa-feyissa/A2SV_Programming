class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backTrack(open, close, path):
            if len(path) == 2 * n:
                answer.append(path)
                return
            if open < n:
                backTrack(open + 1, close, path + "(")
            if open > close:
                backTrack(open, close + 1, path + ")")
        backTrack(0, 0, "")
        return answer
                