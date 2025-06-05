import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
li = []

for _ in range(n):
    w, s, e = map(int, input().split())
    score = e - s + 1
    li.append((w, s, e, score))
cnt = 0

flag=[False]*n

def cal_score(score, c, flag):
    global cnt
    if score == k:
        cnt += 1
        return
    if score > k:
        return
    for i in range(c + 1, n):
        if li[i][0] != 5 and not flag[i]:
            take=True
            for j in range(i):
                if flag[j]:
                    if li[i][0] == li[j][0]:
                        if not (li[i][1] > li[j][2] or li[i][2] < li[j][1]):
                            take=False
                            break
            if take:
                flag[i]=True
                cal_score(score + li[i][3], i, flag)
                flag[i]=False


for i in range(n):
    if li[i][0] != 5:
        flag[i]=True
        cal_score(li[i][3], i, flag)
        flag[i]=False

print(cnt)
