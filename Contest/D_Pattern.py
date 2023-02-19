t = int(input())
data = []
for i in range(t):
    data.append(input())
 
length = len(data[0])
ans=""
for i in range(length):
    count=0
    hash_map = {}
    s = ""
    k = ""
    for j in range(t):
        if data[j][i] == "?":
            hash_map["?"] = 1 + hash_map.get("?", 0)
        elif data[j][i] != "?":
            s = data[j][i]
            hash_map[s] = 1 + hash_map.get(s, 0)
        
    if hash_map.get("?", 0) == t:
        ans+="d"
    elif hash_map.get(s, 0) == t:
        ans+=s
    elif hash_map.get(s, 0) + hash_map.get("?", 0) == t:
        ans+=s
    elif hash_map.get(s, 0) + hash_map.get("?", 0) != t:
        ans+="?"
    else:
        ans+="?"
print(ans)