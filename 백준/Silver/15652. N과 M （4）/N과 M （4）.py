import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N,M=map(int, input().split())

data=[i+1 for i in range(N)]

result = list(combinations_with_replacement(data, M))

for i in result:
    ans=list(i)
    for j in range(len(ans)):
        print(ans[j], end=" ")
    print()



