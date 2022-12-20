# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
word = []
new_dict = {}
for i in range(n):
    x = input()
    if x in new_dict:
        new_dict[x] += 1
    else:
        new_dict[x] = 1
print(len(new_dict.keys()))
print(*new_dict.values())
    
