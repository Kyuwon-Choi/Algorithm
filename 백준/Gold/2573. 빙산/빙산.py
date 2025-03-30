import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    ice_count = [[0] * M for _ in range(N)]
    q = deque([(x, y)])
    visit[x][y]=1
    while q:
        cx, cy = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] and not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                elif not graph[nx][ny]:
                    ice_count[cx][cy] += 1
    for i in range(N):
        for j in range(M):
            graph[i][j]-=ice_count[i][j]
            if graph[i][j]<0:
                graph[i][j]=0

day=0
while True:
    visit = [[0] * M for _ in range(N)]
    flag=0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visit[i][j]:
                bfs(i, j)
                flag=1
                cnt+=1
    if cnt>=2:
        break
    if not flag:
        day=0
        break
    day += 1


print(day)



