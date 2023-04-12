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
  source = []
  sink = []
  for i in range(n):
    if sum(matrix[i]) == 0:
      sink.append(i + 1)
    add = 0
    for j in range(n):
      add += matrix[j][i]
    if add == 0:
      source.append(i + 1)
      
  print(len(source), *sorted(source))
  print(len(sink), *sorted(sink))
T = 1
for ___ in range(T):
  Solve()