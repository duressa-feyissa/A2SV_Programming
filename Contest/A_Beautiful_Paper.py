n = int(input())
for _ in range(n):
    a,b = list(map(int, input().split()))
    c,d = list(map(int, input().split()))
    a, b = max(a,b), min(a,b)
    c, d = max(c,d), min(c,d)
    if a == c and b + d == a:
        print("Yes")
    else:
        print("No")