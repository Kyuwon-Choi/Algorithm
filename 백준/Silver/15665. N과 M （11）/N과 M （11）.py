import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int, input().split()))

li.sort()

cnt=0

ans=[]
def dfs():

    if len(ans)==m:
        print(*ans)
        return

    last=0

    for i in range(n):
        if last != li[i]:
            ans.append(li[i])
            last=li[i]
            dfs()
            ans.pop()


dfs()

