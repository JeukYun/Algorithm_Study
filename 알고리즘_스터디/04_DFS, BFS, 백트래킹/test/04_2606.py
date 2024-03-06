from collections import deque

N = int(input())
E = int(input())

adj = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N + 1)


for _ in range(E):
    y ,x = map(int, input().split())
    adj[y][x] = adj[x][y] = 1

# 인접행렬 확인
# for row in adj:
#     print(row)

# dfs로 구현
def dfs(adj, i, visited):
    visited[i] = True
    for c in range(len(adj[i])):
        if adj[i][c] == 1 and not visited[c]:
            dfs(adj, c, visited)


# bfs로 구현
def bfs(adj, i, visited):
    dq = deque()
    dq.append(i)
    while dq:
        value = dq.popleft()
        if not visited[value]:
            visited[value] = True
        for c in range(len(adj[i])):
            if adj[value][c] == 1 and not visited[c]:
                dq.append(c)



bfs(adj, 1, visited)
print(sum(visited) - 1)