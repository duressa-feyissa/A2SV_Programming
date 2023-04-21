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
  A, B = III()
  if A == B:
    print(A)
  else:
    print(1)
T = 1
for ___ in range(T):
  Solve()
