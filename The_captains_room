# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room = input()
room = list(map(int, room.split()))
new_dict = {}
for r in room:
    if r in new_dict:
        new_dict[r] += 1
    else:
        new_dict[r] = 1
value = 0
for v in new_dict.keys():
    if new_dict[v] == 1:
        value = v
        break
print(value)
