from collections import defaultdict
n = int(input())
array = list(map(int, input().split()))
nums = defaultdict(list)
for n in array:
    if n > 0:
        nums["+"].append(n)
    elif n == 0:
        nums['0'].append(n)
    else:
        nums['-'].append(n)
if len(nums['+']) == 0:
    nums['+'].append(nums['-'].pop())
    nums['+'].append(nums['-'].pop())
if len(nums['-']) % 2 == 0:
    nums['0'].append(nums['-'].pop())
print(len(nums['-']), *nums['-'])
print(len(nums['+']), *nums['+'])
print(len(nums['0']), *nums['0'])

