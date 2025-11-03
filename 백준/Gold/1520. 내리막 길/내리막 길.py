import sys
from collections import deque
import heapq

input = sys.stdin.readline

m, n=map(int, input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int, input().split())))
dp=[[0]*n for _ in range(m)]
dir=[(1,0), (0, 1), (-1, 0), (0, -1)]
dp[0][0]=1

h_graph=[]
for i in range(m):
    for j in range(n):
        h_graph.append((graph[i][j], i, j))

h_graph.sort(key=lambda x: -x[0])

for h, x, y in h_graph:
    for dx, dy in dir:
        nx, ny=x+dx, y+dy

        if 0<=nx<m and 0<=ny<n:
            if graph[x][y]>graph[nx][ny]:
                dp[nx][ny]+=dp[x][y]
print(dp[m-1][n-1])




