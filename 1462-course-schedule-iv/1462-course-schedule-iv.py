class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        distance = [[float('inf')] * numCourses for _ in range(numCourses)]

        for i, j in prerequisites:
            distance[i][j] = 1

        for i in range(numCourses):
            distance[i][i] = 0

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        answer = []
        for start, end in queries:
                answer.append(distance[start][end] != float('inf'))
        return answer
        