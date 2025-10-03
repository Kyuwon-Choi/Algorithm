import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
arr=[]
for _ in range(n):
    d, w=map(int, input().split())
    arr.append((d, w))

arr.sort(key=lambda x:(-x[0], -x[1]))

day=arr[0][0]
ans=0
heap =[]
index=0

for i in range(day, 0, -1):
    while index<n and arr[index][0]>=i:
        heapq.heappush(heap, -arr[index][1])
        index+=1
    if heap:
        ans+=-(heapq.heappop(heap))

print(ans)




