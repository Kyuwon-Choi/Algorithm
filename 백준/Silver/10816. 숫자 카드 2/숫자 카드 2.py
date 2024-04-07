import sys

input = sys.stdin.readline

card={}
n=int(input())
num1=list(map(int, input().split()))
for i in num1:
    if i in card.keys():
        card[i]+=1
    else:
        card[i]=1

m=int(input())
num2=list(map(int, input().split()))
for i in num2:
    if i in card:
        print(card[i], end=" ")
    else:
        print(0, end=" ")

