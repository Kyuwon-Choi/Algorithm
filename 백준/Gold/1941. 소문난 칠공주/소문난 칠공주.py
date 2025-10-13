import sys
from collections import deque

input = sys.stdin.readline

# S - 이다솜, Y - 임도연

# 중복 경우를 어떻게 처리해야할지
graph_2=[]
graph_1=[]
for _ in range(5):
    tmp=list(map(str, input().strip()))
    graph_2.append(tmp)
    graph_1.extend(tmp)

group=[]
global ans
ans=0

def dfs(idx, cnt, s_cnt, group):
    global ans
    if cnt-s_cnt>=4:
        return
    if cnt==7:
        if s_cnt>=4:
            if bfs(group):
                ans+=1
        return
    for i in range(idx, 25):
        if graph_1[i]=='S':
            group.append(i)
            dfs(i+1, cnt+1, s_cnt+1, group)
            group.pop()
        else:
            group.append(i)
            dfs(i + 1, cnt+1, s_cnt, group)
            group.pop()



def bfs(group):
    group_2=[]
    for i in group:
        x=i//5
        y=i%5
        group_2.append((x, y))
    q=deque([group_2[0]])
    visit={group_2[0]}
    while q:
        nx, ny=q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            cx, cy=nx+dx, ny+dy
            if (cx, cy) in group_2 and (cx, cy) not in visit:
                q.append((cx, cy))
                visit.add((cx, cy))

    if len(visit)==7:
        return True
    else:
        return False
dfs(0, 0, 0 ,group)
print(ans)







