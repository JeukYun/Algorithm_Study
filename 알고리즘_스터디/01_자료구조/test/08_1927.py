import sys
import heapq
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    k = int(input())
    if k == 0:
        if len(array): # 1이상인 경우
            print(heapq.heappop(array))
        else:
            print(0)
    elif k:
        heapq.heappush(array, k)