from collections import Counter
from collections import defaultdict
from collections import deque
from itertools import accumulate
 
def I(): return int(input())
def II(): return input()
def III(): return map(int, input().split())
def IV(): return list(map(int, input().split()))
def V(): return sorted(list(map(int, input().split())))

def Solve():
  P, M = III()
  print(min((P + M) // 4, min(P, M)))
T = I()
for ___ in range(T):
    Solve()
