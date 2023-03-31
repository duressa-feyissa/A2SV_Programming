from collections import *
import sys
from functools import reduce
from itertools import *
#Author: Duresa Feyisa

def _input(): return sys.stdin.readline().rstrip("\r\n") 
def I(): return int(_input())
def II(): return _input()
def III(): return map(int, _input().split())
def IV(): return list(map(int, _input().split()))
def V(): return sorted(list(map(int, _input().split())))
def out(var): sys.stdout.write(str(var) + "\n")

def Solve():
  n = I()
  if n == 1:
    print(3)
  else:
    ans = n & -n
    if ans == n:
      print(ans + 1)
    else:
      print(ans)
     
T = I()
for ___ in range(T):
  Solve()
