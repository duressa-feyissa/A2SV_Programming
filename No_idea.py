# Enter your code here. Read input from STDIN. Print output to STDOUT
nums = input()
nums = list(map(int, nums.split()))
n, m = nums[0], nums[1]
check = input()
A = input()
B = input()
check = map(int, check.split())
A = set(map(int, A.split()))
B = set(map(int, B.split()))
add = 0
for i in check:
    if i in A:
        add += 1
    elif i in B:
        add -= 1
print(add)
