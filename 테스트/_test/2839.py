N = int(input())

cnt = 0
if N % 5 == 0: # 5로 나누어 떨어지는 경우
    print(int(N/5)) # 몫 출력
else: # 5로 나누어 떨어지지 않는 경우
    while N % 5: # 나누어 떨어질때까지 반복
        cnt += 1
        N = N - 3
        if N % 5 == 0:
            print(cnt + int(N / 5))
        elif N < 0:
            print(-1)
            break
    