# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

values = list(map(int, input().split()))
m = values[0]
n = values[1]

group_A = defaultdict(list)
for index in range(m):
    value = input()
    group_A[value].append(index + 1)

for index in range(n):
    value = input()
    if value in group_A:
        print(*group_A[value])
    else:
        print(-1)

    

