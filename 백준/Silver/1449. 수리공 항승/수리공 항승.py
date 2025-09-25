import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
hole=list(map(int, input().split()))

hole.sort()

ans=0
index=0
while index<n:
    if index == n - 1:
        ans+=1
        break
    tmp=index
    while hole[index]+l-1>=hole[tmp+1]:
        tmp+=1
        if tmp==n-1:
            break
    index=tmp
    ans+=1
    index+=1

print(ans)

























