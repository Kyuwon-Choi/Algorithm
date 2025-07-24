import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


while True:
    tmp=list(map(int, input().split()))
    n=tmp[0]
    li=tmp[1:]
    if n == 0:
        break
    ans=list(combinations(li, 6))
    for i in ans:
        print(*i)
    print()





