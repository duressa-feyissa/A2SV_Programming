n = int(input())
array = list(map(int, input().split()))
sortedArray = sorted(array)
reversed = False
start = 0
end = 0
for i in range(n):
    if array[i] != sortedArray[i] and not reversed:
        reversed = True
        start = i
    elif array[i] != sortedArray[i] and reversed:
        end = i
temp = array[start: end+1]
temp.reverse()
ans = array[0:start] + temp + array[end+1:]
if ans == sortedArray:
    print('yes')
    print(start + 1, end + 1)
else:
    print("no")
"""
n = int(input())
unsortedArray = list(map(int, input().split()))
sortArray = sorted(unsortedArray)
if sortArray == unsortedArray:
    print("yes")
    print(1, 1)
else:
    i = 0
    j = 0
    for k in range(n):
        if i == 0 and unsortedArray[k] != sortArray[k]:
            i = k
            break
    for k in range(n-1, -1, -1):
        if j == 0 and unsortedArray[k] != sortArray[k]:
            j = k
            break
    a = unsortedArray[:i]
    b = unsortedArray[i:j+1]
    b.reverse()
    c = unsortedArray[j+1:]
    new = a + b +c
    if new == sortArray and i <= j:
        print("yes")
        print("{} {}".format(i+1,j+1))
    else:
        print("no")
"""

