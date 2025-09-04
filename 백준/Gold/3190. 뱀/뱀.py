import sys
from collections import deque

input = sys.stdin.readline
# 0 빈칸, 1 몸뚱아리, 2 사과
n=int(input())
k=int(input())
graph=[[0]*n for _ in range(n)]
for _ in range(k):
    x, y=map(int, input().split())
    graph[x-1][y-1]=2

l=int(input())

turn_count=[]
turn_command=[]
for _ in range(l):
    x, c=map(str, input().split())
    turn_count.append(int(x))
    turn_command.append(c)
dir=[(0,1), (1,0), (0, -1), (-1, 0)]


x, y=0,0
q=deque([(x, y)])
cnt=0
dir_i=0
turn_i=0

while True:
    cnt += 1

    x = x + dir[dir_i][0]
    y = y + dir[dir_i][1]

    if not(0<=x<n and 0<=y<n) or graph[x][y]==1:
        break

    if graph[x][y] == 0:
        graph[x][y] = 1
        q.append((x, y))
        tx, ty = q.popleft()
        graph[tx][ty] = 0

    elif graph[x][y] == 2:
        graph[x][y] = 1
        q.append((x, y))

    if turn_i<len(turn_count):
        if cnt==turn_count[turn_i]:
            if turn_command[turn_i]=='L':
                if dir_i==0:
                    dir_i=3
                else:
                    dir_i-=1
            else:
                if dir_i==3:
                    dir_i=0
                else:
                    dir_i+=1
            turn_i+=1

print(cnt)























