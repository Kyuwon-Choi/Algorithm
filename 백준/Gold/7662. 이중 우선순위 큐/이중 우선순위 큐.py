import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    heap = []
    maxHeap = []
    k = int(input())
    deleted = [0] * k
    for i in range(k):
        operation, num = input().split()
        if operation == 'I':
            elem = int(num)
            heapq.heappush(heap, (elem, i))
            heapq.heappush(maxHeap, (-elem, i))
        elif operation == 'D':
            if num == '-1':
                if heap:
                    deleted[heapq.heappop(heap)[1]]=1
            elif num == '1':
                if maxHeap:
                    deleted[heapq.heappop(maxHeap)[1]] = 1

        while heap and deleted[heap[0][1]] == 1:
            heapq.heappop(heap)
        while maxHeap and deleted[maxHeap[0][1]] ==1:
            heapq.heappop(maxHeap)

    if heap:
        print(-maxHeap[0][0], heap[0][0])
    else:
        print("EMPTY")


