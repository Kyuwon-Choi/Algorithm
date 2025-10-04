import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
    tmp = list(map(str, input().strip()))
    graph.append(tmp)

jx = 0
jy = 0
fire_q = deque([])
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            jx, jy = i, j
        if graph[i][j] == 'F':
            fire_q.append((i, j, 0))
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visit_j = [[False] * c for _ in range(r)]
visit_fire = [[False] * c for _ in range(r)]
fire_time = [[10000] * c for _ in range(r)]


def bfs_fire():
    while fire_q:
        x, y, time = fire_q.popleft()
        visit_fire[x][y] = True
        fire_time[x][y] = time
        for dx, dy in direction:
            if 0 <= x + dx < r and 0 <= y + dy < c and not visit_fire[x + dx][y + dy]:
                if graph[x + dx][y + dy] != '#':
                    visit_fire[x + dx][y + dy] = True
                    fire_q.append((x + dx, y + dy, time + 1))


bfs_fire()

def bfs_j():
    q = deque([(jx, jy, 0)])
    visit_j[jx][jy] = True
    while q:
        x, y, time = q.popleft()
        if x==0 or y==0 or x==r-1 or y==c-1:
            print(time+1)
            return
        for dx, dy in direction:
            if 0 <= x + dx < r and 0 <= y + dy < c and not visit_j[x + dx][y + dy]:
                if graph[x + dx][y + dy] != '#' and fire_time[x + dx][y + dy] > time+1:
                    visit_j[x + dx][y + dy] = True
                    q.append((x + dx, y + dy, time + 1))

    print('IMPOSSIBLE')
    return

if jx == 0 or jy == 0 or jx == r - 1 or jy == c - 1:
    print(1)
else:
    bfs_j()


