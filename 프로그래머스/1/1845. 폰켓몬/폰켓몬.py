from collections import defaultdict
def solution(nums):
    answer = 0
    dic=defaultdict(int)
    for i in nums:
        dic[i]+=1
    if len(dic)<len(nums)/2: 
        answer=len(dic)
    else:
        answer=len(nums)//2
    return answer