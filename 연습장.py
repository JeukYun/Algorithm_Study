# N = int(input())
# S = list(map(int, input().split()))

# occur = [0 for _ in range(200001)] 
# for i in range(N):
#     # abs 함수는 인자로 들어온 수의 절댓값을 반환하는 함수입니다.
#     occur[abs(S[i])] += 1

# print(occur)

# ans = 0
# for i in range(1, 200001):
#     if occur[i] != 1:
#         continue
#     for j in range(N):
#         if abs(S[j]) == i:
#             ans += S[j]
        
# print(ans)

# print((10+2)%10)

lst = [1, 2, 3, 4]
print(lst[-1])