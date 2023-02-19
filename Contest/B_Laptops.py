total_tests = int(input())
data = []
for _ in range(total_tests):
    data.append(list(map(int, input().split())))
data.sort()
count1 = 0
count2 = 0
for i in range(total_tests):
    if data[i][0] > data[i][1]:
        count1 += 1
    if data[i][1] < data[i][0]:
        count2 += 1
if count1 > 0 and count2 > 0:
    print("Happy Alex")
else:
    print("Poor Alex")