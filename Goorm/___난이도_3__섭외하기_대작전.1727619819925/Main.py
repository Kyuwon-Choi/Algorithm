import sys
input = sys.stdin.readline
from bisect import bisect_right

# 한 가수의 영향력이 다른 두 가수의 영향력 합을 넘지 않아야 함 (같은건 가능)
# 섭외 가수는 3명

N= int(input())

S=list(map(int, input().split()))
S.sort()

case=0

for i in range(N-2):
	for j in range(i+1, N-1):
		k=bisect_right(S, S[i]+S[j], j+1)
		case+=k-j-1
		
print(case)

