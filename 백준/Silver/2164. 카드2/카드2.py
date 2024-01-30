import sys
from collections import deque

input = sys.stdin.readline

N=int(input())
card=deque([i+1 for i in range(N)])

while len(card)>1:
    card.popleft()
    tmp=card[0]
    card.append(tmp)
    card.popleft()

print(card.pop())

