from collections import Counter
m, n = map(int, input().split())
string = input()
string_hash = Counter(string)
check = {}
for i in string:
	check[i] = 0
sort_apha = sorted(string_hash.keys())
for i in sort_apha:
	if n - string_hash[i] >= 0:
		check[i] += string_hash[i]
		n = n - string_hash[i]
	else:
		check[i] += n
		n = 0
ans = ""
for i in string:
	if check[i] != 0:
		check[i] -=1
	else:
		ans+=i
print(ans)

"""
from collections import Counter
n, m = map(int, input().split())
str = list(input())
freq = Counter(str)
keys = sorted(freq)
char = ''
val = 0
for k in keys:
    if m:
        if m - freq[k] >= 0:
            m -= freq[k]
            freq[k] = 0
        else:
            char = k
            val = m
            freq[k] -= m
            break
ans = ""
for i in str:
    if freq[i]:
        if char == i and val:
            val -= 1
            continue       
        ans += i
print(ans)
"""