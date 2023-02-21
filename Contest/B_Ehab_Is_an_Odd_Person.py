n = int(input())
array = list(map(int, input().split()))
done = [0, 0]
for i in array:
    done[i % 2] = 1
if done[0] and done[1]:
    array.sort()
print(*array)
