import sys

input = sys.stdin.readline

N=int(input())
arr=set()

for i in range(N):
    arr.add(input().strip())
arr=list(arr)
#사전 정렬 후 길이 정렬
arr.sort()
arr.sort(key = len)

print(*arr, sep='\n')