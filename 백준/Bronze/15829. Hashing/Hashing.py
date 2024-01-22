import sys

input = sys.stdin.readline

r=31
M=1234567891

L=int(input())
str=input()
sum=0
for i in range(L):
    sum+=(ord(str[i])-ord('a')+1) * (r**i)
print(sum)





