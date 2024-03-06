import sys

# 재귀함수의 재귀 횟수 증가(기본값 1000)
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(lambda x : x - 1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1

ans = 0
chk = [False] * N

def dfs(now): 
    for nxt in range(N): 
        
        # 간선이 존재하고, 방문한 적 없는 node인 경우
        if adj[now][nxt] and not chk[nxt]: 
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]: #chk의 i번째가 True가 아닌경우
        ans += 1
        chk[i] = True
        dfs(i) # i(now)가 for문에 의해 0부터 시작

print(ans)