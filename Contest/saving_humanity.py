t = int(input())
for _ in range(t):
    solders, iteration = map(int, input().split())
    iteration = min(iteration, solders)
    array = list(map(int, list(input())))
    carray = array.copy()
    for _ in range(iteration):
        for i in range(solders):
            if i == 0 and array[i] == 0 and array[i + 1] == 1: 
                carray[i] = 1
            elif i == solders - 1 and array[i] == 0 and array[i - 1] == 1:
                carray[i] = 1                
            elif i > 0 and i < solders - 1 and array[i] == 0 and array[i - 1] + array[i + 1] == 1:
                carray[i] = 1
        array = carray.copy()
    print("".join(list(map(str, array))))
 
