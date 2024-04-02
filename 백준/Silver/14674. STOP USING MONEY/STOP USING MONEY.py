import sys
from fractions import Fraction
#파이썬에서 유리수 연산을 정확하게 하려면 fractions.Fraction을 사용해야 한다.
input = sys.stdin.readline

n,k=map(int, input().split())


costList=[]
satisfyList=[]
numList=[]
for i in range(n):
    num, cost, satisfy= map(int, input().split())
    numList.append(num)
    costList.append(cost)
    satisfyList.append(satisfy)

for i in range(n-1):
    for j in range(i+1,n):
        #Fraction
        if Fraction(satisfyList[i],costList[i])<Fraction(satisfyList[j],costList[j]):
            numList[i], numList[j] = numList[j], numList[i]
            satisfyList[i], satisfyList[j] = satisfyList[j], satisfyList[i]
            costList[i], costList[j] = costList[j], costList[i]
        elif Fraction(satisfyList[i],costList[i])==Fraction(satisfyList[j],costList[j]):
            if costList[i]>costList[j]:
                numList[i], numList[j] = numList[j], numList[i]
                satisfyList[i], satisfyList[j] = satisfyList[j], satisfyList[i]
                costList[i], costList[j] = costList[j], costList[i]
            elif costList[i]==costList[j]:
                if numList[i]>numList[j]:
                    numList[i], numList[j] = numList[j], numList[i]
                    satisfyList[i], satisfyList[j] = satisfyList[j], satisfyList[i]
                    costList[i], costList[j] = costList[j], costList[i]

for i in range(k):
    print(numList[i])