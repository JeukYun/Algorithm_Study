# 입력
# N,M : 1~500,000
# my, you : -10,000,000 ~ 10,000,000

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input()) 
my = sorted(list(map(int,input().split())))
M = int(input())
you = list(map(int,input().split()))

ans = []

for y in you:
    r = bisect_right(my, y) 
    l = bisect_left(my, y)
    ans.append(1 if r - l else 0)
        

print(*ans)

# 아래는 시간초과 발생
# ans = [0]*len(you)
# my_s = sorted(my)
# you_s = sorted(you)


# for y in you_s:
#     for m in my_s:
#         if y == m:
#             my_s = my_s[my_s.index(m):]
#             ans[you.index(m)] = 1
#             break
# print(*ans, end = ' ')