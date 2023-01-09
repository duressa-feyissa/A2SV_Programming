from collections import Counter
no_of_tests = int(input())
for test in range(no_of_tests):
    firstLineInput = list(map(int, input().split()))
    planents = firstLineInput[0]
    secondCost = firstLineInput[1]
    secondlineInput = list(map(int, input().split()))
    frequeny = Counter(secondlineInput)
    answer = 0
    for key in frequeny.keys():
        if frequeny[key] == 1:
            answer += 1
        else:
            if secondCost < frequeny[key]:
                answer += secondCost
            else:
                answer += frequeny[key]
    print(answer)
