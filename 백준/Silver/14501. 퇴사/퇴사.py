import sys

input = sys.stdin.readline

N = int(input())
li = [tuple(map(int, input().split())) for _ in range(N)]

max_profit = 0

def dfs(day, total):
    global max_profit

    if day >= N:
        max_profit = max(max_profit, total)
        return

    if day + li[day][0] <= N:
        dfs(day + li[day][0], total + li[day][1])

    dfs(day + 1, total)

dfs(0, 0)

print(max_profit)
