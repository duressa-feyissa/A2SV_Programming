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

def mergeSort(array, left, right, count):
  if left == right:
    return [array[left]]
  middle = (left + right) // 2
  leftSide = mergeSort(array, left, middle, count)
  rightSide = mergeSort(array, middle + 1, right, count)
  if leftSide[0] < rightSide[0]:
    return leftSide + rightSide
  else:
    count[0] += 1
    return rightSide + leftSide

def thereAreSequence(array):
  size = len(array)
  for i in range(1,size):
    if abs(array[i] - array[i - 1]) != 1:
      return False
  return True 

def Solve():
  size = I()
  array = IV()
  count = [0]
  result = mergeSort(array, 0, size - 1, count)
  status = thereAreSequence(result)
  if status:
    print(count[0])
  else:
    print(-1)

T = I()
for ___ in range(T):
  Solve()
