# Enter your code here. Read input from STDIN. Print output to STDOUT
noOfTestCase = int(input())
tests = []
for test in range(noOfTestCase):
    size = int(input())
    data = tuple(map(int, input().split()))
    tests.append([size, data])
    
for value in tests:
    left=0
    right=value[0]-1
    test = value[1]
    stack = []
    while left <= right:
        if test[right] >= test[left]:
            if stack:
                if stack[-1] >= test[right]:
                    stack.append(test[right])
                    right-=1
                else:
                    print("No")
                    break
            else:
                stack.append(test[right])
                right-=1
        else:
            if stack:
                if stack[-1] >= test[left]:
                    stack.append(test[left])
                    left+=1
                else:
                    print("No")
                    break
            else:
                stack.append(test[left])
                left+=1
    else:
        if len(stack) == len(test):
            print("Yes")
        else:
            print("No")
