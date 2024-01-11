key=input()
N=len(key)
code=input()
keyList=list(key)
keySortedList=sorted(keyList)
indexList=sorted(range(N), key=lambda k: keyList[k],reverse=False)
#keyList의 인덱스 배열
orderList=sorted(range(N), key=lambda k: indexList[k],reverse=False)
#indexList의 인덱스 배열

doubleList=[]
i=0
row=len(code)//N
for _ in range(N):
    doubleList.append(list(code[i:i+row]))
    i+=row

doubleList=list(map(list, zip(*doubleList)))
# 행열 변환


for j in range(row):
    for k in orderList:
        print(doubleList[j][k], end="")


                
                
        
        
    


        
