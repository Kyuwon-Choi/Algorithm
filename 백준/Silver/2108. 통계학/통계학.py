import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

li = []

for _ in range(n):
    num = int(input())
    li.append(num)

mostFrequnt=Counter(li).most_common()

frequentList=[]
for i in mostFrequnt:
    if i[1]==mostFrequnt[0][1]:
        frequentList.append(i)

print(round(sum(li) / n))
print(sorted(li)[n // 2])
if len(frequentList)==1:
    print(frequentList[0][0])
else:
    frequentList.sort()
    print(frequentList[1][0])
print(max(li) - min(li))

