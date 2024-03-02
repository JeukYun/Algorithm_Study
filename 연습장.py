from collections import deque

# 0으로 채워진 (13, 13)행렬 생성
adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
# ... 모든 간선 반복

# 방문기록 체크 작성
visited = [False] * 13

# bfs(인접행렬, 시작노드, 방문기록)
def bfs(adj, i, visited):
    dq = deque()
    #root노드 append
    dq.append(i) 
    while dq: # 비어있을때 까지 반복
        value = dq.popleft()
        if not visited[value]:
            print(value, end = ' ')
            visited[value] = True
        for c in range(len(adj[value])):
            # 간선이 있고, 방문한적이 없는경우
            if adj[value][c] == 1 and not visited[c]: 
                dq.append(c) # 다음노드 append

bfs(adj, 0, visited)