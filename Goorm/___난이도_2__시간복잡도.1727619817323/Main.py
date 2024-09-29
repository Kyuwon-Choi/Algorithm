import sys
input = sys.stdin.readline

num=int(input())

ans = 0
for i in range(1, 16):
	ans+=num//(5**i)

print(ans)
