no = int(input())
array = list(map(int, input().split()))
ans = 0
Min = array[0]
Max = array[0]
for i in range(1, no):
    if array[i] < Min:
        ans += 1
        Min = array[i]
    elif array[i] > Max:
        ans += 1
        Max = array[i]
print(ans)