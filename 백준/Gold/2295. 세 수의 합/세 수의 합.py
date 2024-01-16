import sys

N = int(sys.stdin.readline().rstrip())
U = []
for _ in range(N):
    U.append(int(sys.stdin.readline().rstrip()))
U.sort()

sumNum=set()
#집합 사용

for i in U:
    for j in U:
            sumNum.add(i+j)

def answer():
    for k in range(N-1,-1,-1):
        for l in range(k+1):
            if U[k]-U[l] in sumNum:
                return U[k]



print(answer())







