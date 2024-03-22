n = int(input())
count = 0

DP = [0] * (n + 1) # 횟수 저장

k = 1

while k**2 <= n: # n이 제곱수인경우 횟수는 무조건 1회
    DP[k**2] = 1
    k += 1

for i in range(1, n + 1):
    if DP[i] != 0:
        continue
    j = 1
    while j*j <= i:
        if DP[i] == 0: # DP에 값이 저장되어있지 않은 경우
            DP[i] = DP[j*j] + DP[i - j*j] 
        else:
            DP[i] = min(DP[i], DP[j*j] + DP[i - j*j])
        
        j += 1

print(DP[n])