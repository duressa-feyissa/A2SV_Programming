no = int(input())
for _ in range(no):
    rows, cols = list(map(int, input().split()))
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    hash_add = {}
    hash_sub = {}
    for row in range(rows):
        for col in range(cols):
            hash_add[row + col] = hash_add.get(row + col, 0) + matrix[row][col]
            hash_sub[row - col] = hash_sub.get(row - col, 0) + matrix[row][col]
    
    answer = 0
    for row in range(rows):
        for col in range(cols):
            tmp = hash_add[row + col] + hash_sub[row - col] - matrix[row][col]
            answer = max(tmp, answer)    
    
    print(answer)
