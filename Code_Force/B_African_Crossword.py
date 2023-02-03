from collections import Counter
m, n = map(int, input().split())
grid = []
for _ in range(m):
    grid.append(list(input()))
rows = []
for i in range(m):
    rows.append(Counter(grid[i]))
cols = []
for i in list(zip(*grid)):
    cols.append(Counter(i))
string = ""
for i in range(m):
    for j in range(n):
        if rows[i][grid[i][j]] == 1 and cols[j][grid[i][j]] == 1:
            string += grid[i][j]
print(string)    