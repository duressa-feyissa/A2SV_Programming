total_tests = int(input())
for _ in range(total_tests):
    data = list(map(int, input().split()))
    data.sort()
    print(data[1])