import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dont_hear=set()
dont_see=set()

for _ in range(N):
    dont_hear.add(input().strip())
for _ in range(M):
    dont_see.add(input().strip())

dont_see_hear=list(dont_hear&dont_see)
dont_see_hear.sort()
print(len(dont_see_hear))

print(*dont_see_hear, sep='\n')