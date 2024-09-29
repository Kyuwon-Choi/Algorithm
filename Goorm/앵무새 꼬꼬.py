# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline
vowel="aeiouAEIOU"
n = int(input())
for i in range(n):
	ans=""
	str = input()
	for j in str:
		if j in vowel:
			ans += j
	if ans == "":
		ans = "???"
	print(ans)
	
	
