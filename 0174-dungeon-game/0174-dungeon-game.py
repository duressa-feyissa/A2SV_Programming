class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        for i in range(R):
            dungeon[i].append(float('-inf'))
        dungeon.append([float('-inf')] * (C+1))
        dungeon[R][C-1] = 0
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                greater = max(dungeon[i+1][j],  dungeon[i][j+1])
                if dungeon[i][j] < 0:
                    if greater < 0:
                        dungeon[i][j] += greater
                else:
                    if greater < 0 and dungeon[i][j] + greater < 0:
                        dungeon[i][j] += greater
                    else:
                        dungeon[i][j] = 1
        if dungeon[0][0] < 0:
            return -dungeon[0][0] + 1                     
        return 1