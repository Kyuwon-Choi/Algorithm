import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr=[]
for _ in range(n):
    d, w=map(int, input().split())
    arr.append((d, w))
arr.sort(key=lambda x:(-x[0], -x[1]))
queue=deque(arr)
day=queue[0][0]
ans=0
for i in range(day, 0, -1):
    queue2=deque([])
    for j in queue:
        if j[0]>=i:
            if queue2:
                if j[1]>queue2[0][1]:
                    queue2.appendleft(j)
                else:
                    queue2.append(j)
            else:
                queue2.append(j)
    if queue2:
        ans+=queue2[0][1]
        queue.remove(queue2[0])
print(ans)








