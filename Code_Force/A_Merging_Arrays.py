n, m = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
up = 0
down = 0
answer = []
while up < n and down < m:
    if array1[up] >= array2[down]:
        answer.append(array2[down])
        down+=1
    else:
        answer.append(array1[up])
        up+=1
if up == n and down < m:
    answer.extend(array2[down:])
elif down == m and up < n:
    answer.extend(array1[up:])    
print(*answer) 