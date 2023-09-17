import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bomb_cnt = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for _ in range(K):
    y, x = map(int, input().split())
    bomb_cnt[y][x] += 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 1 or nx < 1 or ny > N or nx > N:
            continue
        bomb_cnt[ny][nx] += 1

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        ans += bomb_cnt[i][j]
        
print(ans)