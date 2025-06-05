import sys
from collections import deque

input = sys.stdin.readline

n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

visit=[0]*n
min_cost=float('inf')

def dfs(x, cost, cnt):
    global min_cost

    if cnt==n:
        if graph[x][0]:
            min_cost=min(min_cost, cost+graph[x][0])
        return

    for i in range(1,n):
        if not visit[i] and graph[x][i]:
            visit[i]=1
            dfs(i, cost+graph[x][i], cnt+1)
            visit[i]=0


dfs(0,0,1)
print(min_cost)











