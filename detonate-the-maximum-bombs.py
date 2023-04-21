class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        adjacent = defaultdict(list)
        
        for i in range(N):
            for j in range(i + 1, N):
                x1, x2 = bombs[i][0], bombs[j][0]
                y1, y2 = bombs[i][1], bombs[j][1]
                r1, r2 = bombs[i][2], bombs[j][2]
                distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                if r1 >= distance:
                    adjacent[i].append(j)
                if r2 >= distance:
                    adjacent[j].append(i)

        Max = 1
        def dfs(current, visited):
            visited.add(current)
            count = 1
            for bomb in adjacent[current]:
                if bomb not in visited:
                    count += dfs(bomb, visited)
            return count
        
        for key in list(adjacent.keys()):
            Max = max(Max, dfs(key, set()))

        return Max