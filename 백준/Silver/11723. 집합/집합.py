import sys
from collections import deque
import heapq
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    command_line = input().split()
    command = command_line[0]

    if command == "add":
        x = int(command_line[1])
        S = S | (1 << (x - 1))

    elif command == "remove":
        x = int(command_line[1])
        S = S & ~(1 << (x - 1))

    elif command == "check":
        x = int(command_line[1])
        if (S & (1 << (x - 1))) != 0:
            print(1)
        else:
            print(0)

    elif command == "toggle":
        x = int(command_line[1])
        S = S ^ (1 << (x - 1))

    elif command == "all":
        S = (1 << 20) - 1

    elif command == "empty":
        S = 0