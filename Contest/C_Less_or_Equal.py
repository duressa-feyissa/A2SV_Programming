n , k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
ans = 0
found = True
if n == k:
    ans = array[k - 1]
else:
    if k == 0:
        ans = array[0] - 1
    elif array[k - 1] != array[k]:
        ans = array[k - 1]
    else:
        found = False
if found and ans >= 1 and ans <= 10 ** 9:
    print(ans)
else:
    print(-1)
