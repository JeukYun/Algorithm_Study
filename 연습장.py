# 0으로 채워진 (13, 13)행렬 생성
adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
# ... 모든 간선 반복

# 가독성 좋게 출력
# for row in adj:
#     print(row)

def dfs(now): # now:시작노드
    for nxt in range(13):
        #시작노드 -> 다른 노드로 가는 간선(=1)이 있는경우
        if adj[now][nxt]:
            dfs(nxt) #재귀 호출
            