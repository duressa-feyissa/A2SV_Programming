from collections import Counter
number_test_case = int(input())
for _ in range(number_test_case):
    
    data = input().split()
    hash_map_A = Counter(data[0])
    hash_map_B = Counter(data[1]) 
    answer = {"A": 0, "B": 0}

    if "L" in hash_map_A:
        answer['A'] += 200
        answer['A'] += hash_map_A['X']
    elif "M" in hash_map_A:
        answer['A'] += 100
    elif "S" in hash_map_A:
        answer['A'] -= hash_map_A.get("X", 0)

    if "L" in hash_map_B:
        answer['B'] += 200
        answer['B'] += hash_map_B['X']
    elif "M" in hash_map_B:
        answer['B'] += 100
    elif "S" in hash_map_B:
        answer['B'] -= hash_map_B.get("X", 0)

    if answer['A'] > answer['B']:
        print(">")
    elif answer['A'] < answer['B']:
        print('<')
    else:
        print("=")
