tests = int(input())
for _ in range(tests):
    n = int(input())
    array = list(map(int, input().split()))
    stack = []
    stack.append(array[0])
    left  = 0
    Max = stack[-1]
    if stack[-1] < 0:
        while left < n and array[left] < 0:
            Max = max(array[left], Max)
            left += 1
    else:
        while left < n and array[left] > 0:
            Max = max(array[left], Max)
            left += 1
    stack[-1] = Max
    
    while left < n:
        if stack[-1] < 0:
            stack.append(array[left])
            Max = stack[-1]
            while left < n and array[left] > 0:
                Max = max(array[left], Max)
                left += 1
            stack[-1] = Max
        else:
            stack.append(array[left])
            Max = stack[-1]
            while left < n and array[left] < 0:
                Max = max(array[left], Max)
                left += 1
            stack[-1] = Max
    
    print(sum(stack))
