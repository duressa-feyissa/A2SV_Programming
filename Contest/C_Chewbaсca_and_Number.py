num = list(map(int, list(input())))
for i in range(len(num)):
    if num[i] >= 5:
        if i == 0 and num[i] == 9:
            continue
        num[i] = 9 - num[i]
num = list(map(str, num))
print("".join(num))
