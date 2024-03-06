# 자료 정렬시 튜플도 정렬이 가능하다.
'''
a = [(1,1), (3,2), (2,3), (1,3), (2,1)]
a.sort() 실행 후 a 출력시
[(1,1), (1,3), (2,1), (2,3), (3,2)]

'''

import sys
import heapq as hq

n = int(sys.stdin.readline())

pq = []

for _ in range(n):
    s = int(sys.stdin.readline())
    if s: # 입력값이 0이 아닌경우
        hq.heappush(pq, (abs(s), s)) # 리스트에 (s절대값, s) 튜플삽입
    else: # 입력값이 0인경우
        if pq:
            print(hq.heappop(pq)[1])
        else:
            print('0')

