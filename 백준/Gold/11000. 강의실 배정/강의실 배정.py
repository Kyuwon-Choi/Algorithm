import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
time=[]
for _ in range(n):
    a, b = map(int, input().split())
    time.append((a,b))

time.sort(key=lambda x : (x[0], x[1]))

room=[]
room.append(time[0][1])
room_num=1

for i in range(1, n):
    if room[0]<=time[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappush(room, time[i][1])


print(len(room))