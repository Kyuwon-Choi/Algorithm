import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

n=int(input())
for _ in range(n):
    m=int(input())
    cloth_type=defaultdict(list)
    for _ in range(m):
        name, type = input().split()
        cloth_type[type].append(name)
    cnt=1
    for values in cloth_type.values():
        cnt*=(len(values)+1)
    print(cnt-1)