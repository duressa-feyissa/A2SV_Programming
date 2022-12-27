# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(map(int, input().split()))
N = int(input())
other = []
for element in range(N):
    other.append(set(map(int, input().split())))
for item in other:
    result1 = item.difference(set_A)
    result2 = set_A.difference(item)
    if len(result1) == 0 and len(result2) > 0:
        pass
    else:
        print(False)
        break
else:
    print(True)
