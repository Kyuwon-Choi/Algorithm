import sys
from collections import deque

input = sys.stdin.readline

n, m= map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]

house=[]
chick=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            house.append((i, j))
        elif graph[i][j]==2:
            chick.append((i, j))

visit=[False]*len(chick)
global min_chick_dis
min_chick_dis=float('inf')

def dfs(idx, cnt):
    if cnt==m:
        cal_chick_dis()
        return
    for i in range(idx, len(chick)):
        visit[i]=True
        dfs(i+1, cnt+1)
        visit[i]=False



def cal_chick_dis():
    global min_chick_dis
    sum_dis=0
    for hx, hy in house:
        min_dis=10000000
        for i in range(len(chick)):
            if visit[i]:
                cx, cy=chick[i]
                dis=abs(hx-cx)+abs(hy-cy)
                min_dis=min(min_dis, dis)
        sum_dis+=min_dis
    min_chick_dis=min(min_chick_dis, sum_dis)

dfs(0,0)
print(min_chick_dis)


