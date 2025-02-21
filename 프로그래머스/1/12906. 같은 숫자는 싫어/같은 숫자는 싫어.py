from collections import deque

def solution(arr):
    answer = []
    queue=deque([arr[0]])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            queue.append(arr[i])
    answer=list(queue)
    return answer