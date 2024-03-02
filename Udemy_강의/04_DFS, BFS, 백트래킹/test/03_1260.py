import sys
from collections import deque

N, M, V = map(int, input().split())
# 정점, 간선, 탐색시작번호 확인
# print(N, M, V)
adj = [[0] * (N+1) for _ in range(N+1)]

# 방문한 곳 체크
visited = [False] * (N+1)
# print(visited)

for _ in range(M):
    y, x = map(int, sys.stdin.readline().split())
    adj[y][x] = adj[x][y] = 1


# # 인접행렬 확인
# for row in adj:
#     print(row)

def dfs(adj, i, visited):
    visited[i] = True # 방문한 곳 체크
    print(i, end = ' ') 
    for c in range(len(adj[i])):
        # 간선이 있고, 방문한적이 없는 경우
        if adj[i][c] == 1 and not visited[c]:
            # 재귀함수 호출
            dfs(adj, c, visited)


def bfs(adj, i, visited):
    dq = deque()
    dq.append(i)
    while dq:
        value = dq.popleft()
        if not visited[value]:
            print(value, end = ' ')
            visited[value] = True
            for c in range(len(adj[value])):
                if adj[value][c] == 1 and not visited[c]:
                    dq.append(c)


dfs(adj, V, visited)
visited = [False] * (N+1)
print()
bfs(adj, V, visited)