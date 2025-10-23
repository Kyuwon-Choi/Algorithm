import sys
from collections import deque
import heapq

input = sys.stdin.readline

n=int(input())

dp=[0]*(n+1)

dp[0]=1
if n>1:
    dp[2]=3

for i in range(4, n+1, 2):
    dp[i]=4*dp[i-2]-dp[i-4]
print(dp[n])



