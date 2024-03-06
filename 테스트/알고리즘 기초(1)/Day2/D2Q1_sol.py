# best code!

S = list(map(int, input().split()))
S.sort() # 큰수부터 정렬
print(S[3] + S[2] - S[1] - S[0])
# 큰수끼린 +, 작은수는 - 
# 주어지는 정수가 양수이므로 가능!





# so1 2.
S = list(map(int, input().split()))
ans = 0
for a in S:
    x1 = a
    for b in S:
        # 수를 중복해서 사용하면 안 된다!
        if a == b:
            continue # a,b가 중복 된 경우 아래 코드를 건너뛰고 for문의 처음으로 돌아감
        y1 = b
        for c in S:
            if a == c or b == c:
                continue
            x2 = c
            for d in S:
                if a == d or b == d or c == d:
                    continue
                y2 = d
                # 맨해튼 거리 계산
                dist = abs(x1 - x2) + abs(y1 - y2)
                # 가장 큰 값으로 정답 갱신
                ans = max(ans, dist)

print(ans)

