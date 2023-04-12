from collections import *

def I(): return int(input())
def IV(): return list(map(int, input().split()))

def Solve():
  V = I()
  k = I()
  matrix = defaultdict(list)
  for _ in range(k):
    op = IV()
    if len(op) == 3:
      matrix[op[1]].append(op[2])
      matrix[op[2]].append(op[1])
    else:
      print(*matrix[op[1]])

T = 1
for ___ in range(T):
  Solve()