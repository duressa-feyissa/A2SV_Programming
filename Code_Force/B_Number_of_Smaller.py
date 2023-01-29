m, n = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
up=0
bottom=0
while bottom < n:
    if up < m and array1[up] < array2[bottom]:
        up += 1
    else:
        print(up, end=" ")
        bottom += 1



