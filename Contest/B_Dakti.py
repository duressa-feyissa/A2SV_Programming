t = int(input())
for i in range(t):
    hash_map = {}
    data = input().split()
    alpa = [chr(i) for i in range(97, 123)]
    number = set(["1", "2","3", "4","5","6","7","8","9","0"])
    alpha = set(alpa)
    for item in data:
        numb=""
        string = ""
        for i in item:
            if i in number:
                numb+=i
            else:
                string += i
        numb = int(numb)
        hash_map[numb] = string
    tmp = hash_map.keys()
    tmp = list(tmp)
    tmp.sort()
    a = [hash_map[i] for i in tmp]
    print(" ".join(a))

"""
no = int(input())
check = set([str(i) for i in range(0,10)])
for _ in range(no):
    words = input().split()
    hash_word = {}
    for word in words:
        num = ""
        temp = ""
        for c in word:
            if c in check:
                num += c
            else:
                temp += c
        hash_word[int(num)] = temp
    ans = []
    for k in sorted(hash_word.keys()):
        ans.append(hash_word[k])
    print(*ans)
"""
