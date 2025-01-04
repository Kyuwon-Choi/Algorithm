import sys
from collections import deque
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()


combs = set(itertools.combinations_with_replacement(num, M))

sorted_combs = sorted(combs)

for comb in sorted_combs:
    print(" ".join(map(str, comb)))



