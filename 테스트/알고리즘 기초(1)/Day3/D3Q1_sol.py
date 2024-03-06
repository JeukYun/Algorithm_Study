# best
f_num = int(input())
f_score = list(map(int,input().rstrip().split()))
print(sum(f_score))

####################################################################

# sol 1
N = int(input())
S = list(map(int, input().split()))

occur = dict()
for i in range(N):
    # 현재 점수가 존재하는지를 occur에 기록해둡니다.
    occur[S[i]] = 1
    # occur[S[i]]에 해당하는 key의 value 값 : 1

print(occur)

ans = 0
for i in range(N):
    # 각 점수마다 부호가 반대인 점수 값이 occur에 존재하는지를 확인합니다.
    # key 값이 존재하는 경우에는 소개팅을 진행할 수 있다는 뜻이니, 넘어가줍시다.
    if -S[i] not in occur:
        ans += S[i]
        
print(ans)


################################################################

# sol 2
N = int(input())
S = list(map(int, input().split()))

occur = [0 for _ in range(200001)] #20만개의 0으로 채워진 list
for i in range(N):
    occur[abs(S[i])] += 1

ans = 0
for i in range(1, 200001):
    if occur[i] != 1:
        continue
    for j in range(N):
        if abs(S[j]) == i:
            ans += S[j]
        
print(ans)