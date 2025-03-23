import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph=[]
for i in range(N):
    graph.append(list(map(int, input().split())))



def bfs(x, y):
    visit = [[0] * M for _ in range(N)]
    c = [[0] * M for _ in range(N)]
    c_list=[]
    q = deque([(x, y)])
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ((0,1), (1,0), (-1,0), (0,-1)):
            cx, cy=dx+x, dy+y
            if 0<=cx<N and 0<=cy<M:
                if graph[cx][cy]:
                    c[cx][cy] += 1
                    if c[cx][cy]>=2:
                        c_list.append((cx,cy))
                if not graph[cx][cy] and not visit[cx][cy]:
                    q.append((cx, cy))
                    visit[cx][cy]=1
    for i,j in c_list:
        graph[i][j]=0


cnt=0

for i in range(N):
    for j in range(M):
        if graph[i][j] ==1:
            cnt+=1
            bfs(0,0)


print(cnt)

