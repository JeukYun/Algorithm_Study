N = int(input())

for i in range(1, N+1): #1~N까지 반복
    n_sum = sum(map(int, str(i)))
    M = n_sum + i
    if M == N: #
        print(N - n_sum)
        break
    elif i == N:
        print(0)
