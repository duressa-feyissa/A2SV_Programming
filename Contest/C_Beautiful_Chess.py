n = int(input())
for _ in range(n):
    matrix = []
    a = input()
    for _ in range(8):
        matrix.append(list(input()))
    done=False
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == "#":
                if i > 0 and j > 0 and j + 1 < 8 and i + 1 < 8:
                    if matrix[i+1][j+1] == "#" and matrix[i - 1][j + 1] == "#":
                        print(i+1, j+1)
                        done=True
        if done:
            break