import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic={}
for _ in range(N):
    tmp1, tmp2=input().split()
    dic[tmp1]=tmp2
for _ in range(M):
    site=input().strip()
    print(dic[site])
