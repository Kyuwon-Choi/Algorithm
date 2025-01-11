import sys
from collections import deque
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())

graph=[[False] *(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v]=1
    graph[v][u]=1


visited=[False] *(N+1)
def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v=queue.popleft()
        for i in range(1, N+1):
            if not visited[i] and graph[v][i]==1:
                queue.append(i)
                visited[i]=True
cnt=0

for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        cnt+=1

print(cnt)
