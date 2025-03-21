import sys
from collections import deque

input = sys.stdin.readline

N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int, input().strip())))

visit=[[False for _ in range(N)] for _ in range(N)]


def bfs(x, y):
    queue=deque([(x,y)])
    visit[x][y]=True
    length=1
    while queue:
        nx, ny = queue.popleft()
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            cx, cy= nx+dx,ny+dy
            if 0<=cx<N and 0<=cy<N:
                if not visit[cx][cy] and graph[cx][cy]:
                    queue.append((cx, cy))
                    visit[cx][cy] = True
                    length+=1
    return length

cnt=0
cnt_arr=[]
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visit[i][j]:
            cnt+=1
            cnt_arr.append(bfs(i, j))
print(cnt)
cnt_arr.sort()
for i in cnt_arr:
    print(i)




