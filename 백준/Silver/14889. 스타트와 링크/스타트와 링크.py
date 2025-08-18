import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
team=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    team.append(tmp)

global min_diff
min_diff=1000000

visit=[False]*n
def dfs(idx, cnt):
    global min_diff
    if min_diff==0:
        return
    if cnt==n//2:
        cal_min()
    for i in range(idx, n):
        if not visit[i]:
            visit[i]=True
            dfs(i+1, cnt+1)
            visit[i]=False

def cal_min():
    global min_diff
    total1=0
    total2=0

    for i in range(n):
        for j in range(i+1, n):
            if visit[i] and visit[j]:
                total1+=team[i][j]+team[j][i]
            elif not visit[i] and not visit[j]:
                total2+=team[i][j]+team[j][i]
    min_diff=min(min_diff, abs(total2-total1))



dfs(0, 0)
print(min_diff)



