# 1 : 1 2 3 4 5 6 7 8 9 
# 2 : 10 12 23 34 45 56 67 78 89 21 32 43 54 65 76 87 98 

# cache[n][d] : 길이가 n, 마지막 숫자가 d인 계단수의 갯수
cache = [[0] * 10 for _ in range(101)] #

for j in range(1, 10): 
    cache[1][j] = 1 # 길이가 1, 끝자리가 d인 수는 모두 1이므로
# d가 주어졌을때 
# d가 1~8 : d+1은 d에서 +1 or -1가능
# d가 0 : d+1은 1만 가능
# d가 9 : d+1은 8만 가능

for i in range(2, 101): # n = 1인경우 채워졌으므로 2~100
    for j in range(10):
        if j == 0:
            cache[i][j] = cache[i-1][1] # 끝자리가 0인경우 1만 가능
        elif j == 9:
            cache[i][j] = cache[i-1][8] # 끝자리가 9인경우 8만 가능
        else:
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j+1]
MOD = 1000000000
print(sum(cache[int(input())]) % MOD)