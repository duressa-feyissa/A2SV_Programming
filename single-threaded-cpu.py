class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        array = []
        for i in range(N):
            array.append((tasks[i][0], tasks[i][1], i))
        tasks  = sorted(array)
        time = 0
        array = []
        answer = []
        i = 0
        while i < N:
            if not array:
                time = max(tasks[i][0], time)
                while i < N and time == tasks[i][0]:
                    heappush(array, (tasks[i][1], tasks[i][2]))
                    i += 1
            else:
                period, index = heappop(array)
                answer.append(index)
                time += period
                while i < N and time >= tasks[i][0]:
                    heappush(array, (tasks[i][1], tasks[i][2]))
                    i += 1
        while array:
            _, index = heappop(array)
            answer.append(index)
        return answer