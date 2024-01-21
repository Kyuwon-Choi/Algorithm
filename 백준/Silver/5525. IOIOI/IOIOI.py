import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

cnt, index, ans = 0, 0, 0

while index < (M-1):
    if S[index:index+3] == "IOI":
        index += 2
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        index += 1
        cnt = 0

print(ans)



