import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  q = deque([(x, y)])
  visited[x][y] = True
  while q:
    cx, cy = q.popleft()
    for dx, dy in directions:
      nx, ny = cx + dx, cy + dy
      if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
        q.append((nx, ny))
        visited[nx][ny] = True

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  graph = []
  for _ in range(h):
      row = list(map(int, input().split()))
      graph.append(row)

  visited = [[False] * w for _ in range(h)]

  cnt = 0
  for i in range(h):
      for j in range(w):
          if not visited[i][j] and graph[i][j] == 1:
              bfs(i, j)
              cnt += 1

  print(cnt)


