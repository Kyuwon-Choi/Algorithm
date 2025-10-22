import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
date=[]

for _ in range(n):
    tmp=list(map(int, input().split()))
    date.append(tmp)

date.sort(key=lambda x : (x[2], x[3]))
ans=0
index=0
mon, day=3, 1
while mon<=11:
    tmp=-1
    for i in range(index+1, len(date)):
        if date[i][0]<mon or (date[i][0]==mon and date[i][1]<=day):
            tmp=i
    if tmp ==-1:
        ans=0
        break
    index = tmp
    ans += 1
    mon = date[tmp][2]
    day = date[tmp][3]

print(ans)



