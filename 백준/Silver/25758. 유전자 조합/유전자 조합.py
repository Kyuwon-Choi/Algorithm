import sys
input = sys.stdin.readline

# 첫번째 유전자의 첫번째 형질, 두번째 유전자의 두번째 형질
# 사전순으로 큰 것이 표현형

N = int(input())
G = input().split()

from collections import defaultdict
#collections.defaultdict - 딕셔너리 한번에 초기화
first = defaultdict(int)
second = defaultdict(int)

for g in G:
    first[g[0]] += 1
    second[g[1]] += 1

answer = set()
for g in G:
    f, s = g[0], g[1]
    for k in first:
        if k <= s and first[k] > 0:
            if f != k:
                answer.add(s)
            elif f == k and first[k] > 1:
                answer.add(s)
    for k in second:
        if k <= f and second[k] > 0:
            if s != k:
                answer.add(f)
            elif s == k and second[k] > 1:
                answer.add(f)

print(len(answer))
print(*(sorted(answer)))
