import sys
from collections import deque
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())

num = [i for i in range(1, N+1)]
nPr = itertools.permutations(num, M)

for perm in nPr:
    print(" ".join(map(str, perm)))