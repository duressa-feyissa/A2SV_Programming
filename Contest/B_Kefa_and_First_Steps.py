no = int(input())
array = list(map(int, input().split()))
array.append(-1)
ans = 1
right = 1
left = 0
while right < no + 1:
    if array[right - 1] <= array[right]:
        right += 1
    else:
        temp = right - left
        left = right
        right += 1
        ans = max(temp, ans)
print(ans)
