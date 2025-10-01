import sys
from collections import deque

input = sys.stdin.readline

n= int(input())

arr=[]

for _ in range(n):
    a, b= map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))

ans=1
end=arr[0][1]
for i in range(1, len(arr)):
    if arr[i][0]>=end:
        ans+=1
        end=arr[i][1]
print(ans)

