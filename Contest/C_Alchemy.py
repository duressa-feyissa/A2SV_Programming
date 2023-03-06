n = int(input())
array = list(map(int, input().split()))
l, r = 0, n - 1
lsum, rsum = 0, 0
while l <= r:
    if lsum <= rsum:
        lsum += array[l]
        l += 1
    else:
        rsum += array[r]
        r -= 1
print(l, n - l)