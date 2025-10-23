import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
dp=[100001]*(k+1)
dp[0]=0

for i in range(1, k+1):
    for j in arr:
        if i >= j:
            dp[i]=min(dp[i], dp[i-j]+1)
if dp[k]==100001:
    print(-1)
else:
    print(dp[k])


