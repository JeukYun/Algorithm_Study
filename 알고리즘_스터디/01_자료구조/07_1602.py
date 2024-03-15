import sys
input = sys.stdin.readline

N, M = map(int, input().split())

P_dic = {}

for i in range(1, N+1):
    p = input().rstrip()
    P_dic[i] = p
    P_dic[p] = i

for _ in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(P_dic[int(q)])
    else:
        print(P_dic[q])