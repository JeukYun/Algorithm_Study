
'''
스택(배열)으로 풀이 -> 시간초과 발생 
1. 맨 앞의 값을 삭제
2. 맨 앞의 값을 맨 뒤로 보내기 -> 삭제 후 삽입 

삭제 2번, 삽입 1번..
시간복잡도가 N^2 
'''

# import sys
# n = int(sys.stdin.readline())

# STK = [] # 빈스택 생성

# for i in range(n, 0, -1):
#     STK.append(i)

# print(STK)
# while len(STK) > 1:
#     STK.pop()

#     top = STK.pop()

#     new_STK = [] # 새로운 빈스택 생성
#     new_STK.append(top)

#     for i in STK:
#         new_STK.append(i)
#     STK = new_STK
#     print(STK)

# print(STK.pop())


# 큐로 풀어야 함.
import sys
from collections import deque # 큐역할을 하는 모듈 deque 호출

n = int(sys.stdin.readline())

dq = deque(range(1, n+1)) # 덱 생성 및 삽입

while len(dq) > 1:
    dq.popleft() # 가장 앞 숫자 버리기

    change_n = dq.popleft() # 가장 앞숫자 뒤로 보내기
    dq.append(change_n) 
    # dq.append(dq.popleft()) 도 가능

print(dq.pop())

