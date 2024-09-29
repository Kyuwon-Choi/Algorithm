# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline
from collections import defaultdict


a, b = map(int, input().split())

# dic = defaultdict(int)
# for i in range(a, b+1):
# 	for j in range(2, int(i**(1/2))+1): #실행시간을 줄이기 위함
# 		if i % j == 0:
# 			dic[j] += 1
# 			if j != i//j:
# 				dic[i//j]+=1
# 	dic[i]+=1
# max_value = max(dic.values())
# smallest_max_divisor = min([k for k, v in dic.items() if v == max_value])

# print(smallest_max_divisor)

#greedy
if a != b:
	print(2)
	
else:
	ans=0
	for i in range(2, int(a**(1/2)) + 1):
		if a%i == 0:
			ans = i
			break
	if ans ==0 :
		print(a)

	else:
		print(ans)



			