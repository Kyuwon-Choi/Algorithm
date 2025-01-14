import sys
from collections import deque
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
graph=[]

for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

visited = [[False]*m for _ in range(n)]

def bfs(x, y):
    direction = [(-1, 0),(1, 0),(0, 1),(0, -1)]
    len=0
    queue=deque([(x, y)])
    visited[x][y] = True
    len+=1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in direction:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny]=True
                len+=1

    return len

cnt = 0
max = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            len=bfs(i, j)
            cnt+=1
            if max<len:
                max=len
print(cnt)
print(max)





