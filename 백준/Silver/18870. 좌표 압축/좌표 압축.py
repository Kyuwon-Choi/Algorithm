import sys
input = sys.stdin.readline

n=int(input())

inputList=list(map(int, input().split()))

#집합, 딕셔너리 사용
sortedList=sorted(set(inputList))
dict={sortedList[i]:i for i in range(len(sortedList))}

#딕셔너리의 키를 인풋리스트에서 가져오기
for i in inputList:
    print(dict[i], end=" ")

















