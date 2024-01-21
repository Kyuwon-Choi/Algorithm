import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

P= "IO"*N +"I"
cnt=0
tmp=0
for _ in range(M-(2*N+1)+1):
    if P not in S:
        break
    index = S.find(P, tmp)
    if index == -1:
        break
    tmp=index+2
    cnt += 1

print(cnt)



