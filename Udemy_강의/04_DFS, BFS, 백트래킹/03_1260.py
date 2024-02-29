import sys
from collections import deque

N, M, V = map(int, input().split())
# 정점, 간선, 탐색시작번호 확인
# print(N, M, V)

adj = [[False] * N for _ in range(N)]

for _ in range(M):
    y, x = map(int, sys.stdin.readline().split())
    y -= 1
    x -= 1
    adj[y][x] = True


# 인접행렬 확인
for row in adj:
    print(row)



def dfs(now):
    print(now)
    for nxt in range(N):
        if adj[now][nxt]:
            dfs(nxt) # 재귀호출

def bfs(V):
    dq = deque()
    dq.append(V) # 시작노드 추가
    bfs_list.append(V) # 리스트에 추가
    while dq: #비어있을때까지 반복
        now = dq.popleft()

        for nxt in range(N):
            if adj[now][nxt]: # 간선이 있으면
                dq.append(nxt)
