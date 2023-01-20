total_tests = int(input())
for _ in range(total_tests):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    prev = 0
    next = 1
    while next < n and abs(nums[prev] - nums[next]) <= 1:
        next += 1
        prev+=1
    if prev == n - 1:
        print("YES")
    else:
        print("NO")
