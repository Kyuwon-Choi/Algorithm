def getRandomNum(num):
    numList=[num]
    while True:
        powerList=[]
        numPower=num**2
        while numPower>0:
            powerList.append(numPower%10)
            numPower//=10
        if len(powerList)==8:
            powerList.reverse()
        else:
            while len(powerList)<8:
                powerList.append(0)
            powerList.reverse()
        randNum=powerList[2]*1000+powerList[3]*100+powerList[4]*10+powerList[5]
        if randNum in numList:
            return len(numList)
        numList.append(randNum)
        num=randNum
        
while True:
    n=int(input())
    if n==0:
        break
    randNumCnt=getRandomNum(n)
    print(randNumCnt)
        
    
    
        


    
        
    
        
        

    
    
