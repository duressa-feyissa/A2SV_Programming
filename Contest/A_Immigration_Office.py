n = int(input())
queue = list(map(str, input().split()))
test = int(input())
for _ in range(test):
    search = input()
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if queue[middle] <= search:
            left = middle + 1
        else:
            right = middle - 1
    print(left)