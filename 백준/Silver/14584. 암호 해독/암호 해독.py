def findOriginal(word, code):
    for i in range(26):
        temp=""
        for j in code:
            temp+=chr((ord(j)-ord('a')+i)%26+ord('a'))
            #파이썬에서 아스키코드 변환 함수 -> ord
            #아스키코드에서 문자로 변환 함수 -> chr

        if word in temp:
            return temp

    return None
    
code=input()
wordNumbers=int(input())
wordList=[]


for _ in range(wordNumbers):
    wordList.append(input())
    

for i in range(wordNumbers):
    result = findOriginal(wordList[i], code)
    
    if result:
        print(result)
        break