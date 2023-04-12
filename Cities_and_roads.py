from collections import *
import sys
from functools import reduce
from itertools import *

def _input(): return sys.stdin.readline().rstrip("\r\n") 
def I(): return int(_input())
def II(): return _input()
def III(): return map(int, _input().split())
def IV(): return list(map(int, _input().split()))
def V(): return sorted(list(map(int, _input().split())))
def out(var): sys.stdout.write(str(var) + "\n")


def Solve():
  n = I()
  matrix = []
  for i in range(n):
    matrix.append(IV())
  count = 0
  for i in range(n):
    for j in range(n):
      if matrix[i][j]:
        count += 1
        matrix[j][i] = 0
  out(count)
T = 1
for ___ in range(T):
  Solve()