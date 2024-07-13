import sys
input = sys.stdin.readline

# 재료 개수, 혀용되는 총 세균 수, 뺄 수 있는 재료 수
N, G, K = map(int, input().split())

# 부패 속도, 유통기한, 중요재료 여부
important_s=[]
important_l=[]
unimportant_s=[]
unimportant_l=[]
# x일의 세균수 - S*(max(1, x-L))
max_b=0
for _ in range(N):
    a, b, c = map(int, input().split())
    if c:
        unimportant_s.append(a)
        unimportant_l.append(b)
    else:
        important_s.append(a)
        important_l.append(b)

start, end = 1, int(2e9) # 최대 날짜

while start<=end:
    mid = (start + end) // 2
    total_bac=0
    unimportant_bac=[]
    important_bac=0
    for i in range(len(important_l)):
        if mid - important_l[i] <=1:
            important_bac+=important_s[i]
        else:
            important_bac+=important_s[i]*(mid-important_l[i])
    for i in range(len(unimportant_l)):
        if mid - unimportant_l[i] <=1:
            unimportant_bac.append(unimportant_s[i])
        else:
            unimportant_bac.append(unimportant_s[i]*(mid-unimportant_l[i]))
    unimportant_bac.sort()
    unimportant_sum=sum(unimportant_bac[:len(unimportant_bac)-K])
    total_bac = important_bac+unimportant_sum
    if total_bac > G:
        end = mid - 1
    else:
        start = mid + 1


print(end)













