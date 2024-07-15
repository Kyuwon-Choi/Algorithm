import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int, input().split()))
M=int(input())
B=list(map(int, input().split()))
# B가 A안에 존재하는지
A.sort()

for i in B:
    start, end = 0, N-1
    if i<A[start] or i>A[end]:
        print(0)
        continue
    while start<=end:
        mid = (start + end) // 2
        if A[mid]<i:
            start=mid+1
        elif A[mid]>i:
            end=mid-1
        else:
            print(1)
            break
    if start>end:
        print(0)


