import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph=[]

for i in range(N):
    li = list(map(int, input().strip()))
    graph.append(li)

visited=[[False]*(M) for _ in range(N)]


def bfs(x, y):
    direction=[(1, 0),(0, 1),(-1, 0),(0, -1)]
    visited[x][y]=True
    queue=deque([(x, y, 1)])
    while queue:
        cx, cy, length= queue.popleft()
        for dx, dy in direction:
            nx=dx+cx
            ny=dy+cy
            if nx == N-1 and ny == M-1:
                return length+1
            elif 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny, length+1))
                    visited[nx][ny]=True

print(bfs(0,0))


