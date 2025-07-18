import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
visit = [False] * n
ans=[]

def dfs():
    if len(ans) == m:
        print(*ans)
        return

    last = 0

    for i in range(n):
        if not visit[i] and last != li[i]:
            visit[i] = True 
            ans.append(li[i])  
            last = li[i] 
            dfs() 
            ans.pop()
            visit[i] = False

dfs()