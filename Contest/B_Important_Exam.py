n, m = map(int, input().split())
students = []
posibilities = {'A':0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
for _ in range(n):
    students.append(input())
points = list(map(int, input().split()))
total = 0
for i in range(m):
    ans = [0,0,0,0,0]
    for j in range(n):
        ans[posibilities[students[j][i]]] += 1
    total += max(ans) * points[i]
print(total)
