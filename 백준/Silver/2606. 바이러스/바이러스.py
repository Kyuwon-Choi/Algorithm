import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
e = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
for i in range(e):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1

visited = [False] * (n+1)

def bfs(v):
  q = deque([v])

  visited[v] = True

  while q:
    v = q.popleft()
    for i in range(1, n+1):
      if not visited[i] and graph[v][i] == 1:
        q.append(i)
        visited[i] = True



bfs(1)
cnt=0

for i in visited:
  if i:
    cnt+=1

print(cnt-1)


