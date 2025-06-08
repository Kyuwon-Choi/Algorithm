import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

li=list(map(int, input().split()))

ans=list(set(permutations(li,m)))

ans.sort()
for i in ans:
    print(*i)

