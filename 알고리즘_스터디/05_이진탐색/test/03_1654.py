import sys
input = sys.stdin.readline

# 이분탐색 parametric search
# 가능하면 True, 불가능하면 False

K, N = map(int, input().split())
# print(K,N)

lan = []
for _ in range(K):
    lan.append(int(input()))

low = 1
high = max(lan)
mid = high // 2

def is_lans(X):
    global N, mid
    sum_list = []

    for x in X:
        sum_list.append(x // mid) 
    if sum(sum_list) >= N:
        return True

if mid == 0:
    print(high)
else:
    while high >= low:
        if is_lans(lan):
            low = mid + 1
        else:
            high = mid - 1

        mid = (low + high) // 2

    print(high)
