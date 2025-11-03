import sys
from collections import deque
import heapq
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

m, n=map(int, input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int, input().split())))
dp=[[-1]*n for _ in range(m)]
dir=[(1,0), (0, 1), (-1, 0), (0, -1)]
global cnt
cnt=0

def recur(x, y):
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]

    dp[x][y] = 0

    cnt=0
    for dx, dy in dir:
        if 0<=x+dx<m and 0<=y+dy<n:
            if graph[x][y]>graph[x+dx][y+dy]:
                cnt+=recur(x+dx, y+dy)
    dp[x][y]=cnt
    return dp[x][y]


print(recur(0,0))