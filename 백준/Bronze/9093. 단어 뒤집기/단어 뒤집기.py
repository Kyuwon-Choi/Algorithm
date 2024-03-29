import sys

input = sys.stdin.readline

n=int(input())

list=[]
for i in range(n):
    list.append(input().split())
    for j in range(len(list[i])):
        print(list[i][j][::-1], end=" ")
    print()






