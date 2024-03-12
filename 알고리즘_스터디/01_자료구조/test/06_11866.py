from collections import deque

N, K = map(int, input().split())
K -= 1
dq = deque(i for i in range(1, N + 1))

res = []
while len(dq):
    for _ in range(K):
        dq.append(dq.popleft())
    res.append(str(dq.popleft()))

print('<' +', '.join(res) + '>')