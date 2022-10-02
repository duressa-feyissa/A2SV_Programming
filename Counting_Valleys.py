#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    U = 0
    D = 0
    V = 0
    hold = path[0]
    for i in range(len(path)):
        if path[i] == "D":
            D += 1
        if path[i] == "U":
            U += 1
        if D == U:
            if hold == "D":
                V += 1
            if steps != i + 1:
                hold = path[i + 1]
    return V

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
