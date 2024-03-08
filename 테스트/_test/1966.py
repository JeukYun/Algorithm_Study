from collections import deque

T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    M = list(map(int, input().split()))

    dq = deque()
    for i, lst in enumerate(M):
        dq.append((lst, i))

    count = 0

    while True:
        if dq[0][0] == max(dq)[0]:
            count += 1
            if dq[0][1] == k:
                print(count)
                break
            else:
                dq.popleft()
        else:
            dq.append(dq.popleft())
    