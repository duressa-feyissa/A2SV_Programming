#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    j = n - 2
    num = arr[n-1]
    while j >= 0:
        if arr[j] > num:
            arr[j + 1] = arr[j]
            print(" ".join(map(str, arr)))
            if j == 0:
                arr[j] = num
                print(" ".join(map(str, arr))) 
        else:
            arr[j + 1] = num
            print(" ".join(map(str, arr)))
            break
        j -= 1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
