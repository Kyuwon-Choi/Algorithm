import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a<b:
	if c in range(a,b+1):
		print("No")
	else:
		print("Yes")
		
else:
	if c in range(a, 24) or c in range(0, b+1):
		print("No")
	else:
		print("Yes")
		
