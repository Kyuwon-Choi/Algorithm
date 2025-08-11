import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int, input().split()))

li.sort()

visit=[False]*n
cnt=0

ans=[]
def dfs(i):

    if len(ans)==m:
        print(*ans)
        return

    last=0

    for i in range(i, n):
        if not visit[i] and last != li[i]:
            ans.append(li[i])
            visit[i]=True
            last=li[i]
            dfs(i)
            ans.pop()
            visit[i]=False


dfs(0)










