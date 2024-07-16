import sys
input = sys.stdin.readline

N, M = map(int, input().split())
str=set()

cnt=0
for _ in range(N):
    str.add(input())
for _ in range(M):
    ans=input()
    if ans in str:
        cnt+=1

print(cnt)