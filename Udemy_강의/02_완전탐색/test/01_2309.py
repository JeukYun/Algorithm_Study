from itertools import combinations
# 중복 비허용이므로 combinations

# lst = []
# for _ in range(9):
#     lst.append(int(input()))

# 아래와 같이 단순화 가능
lst = [int(input()) for _ in range(9)]

for comb in combinations(lst, 7):
    if sum(comb) == 100: # 튜플의 합이 100인경우

        # 튜플 정렬함수 : sorted()
        for i in sorted(comb):
            print(i)
        break # break가 없는경우, 중복답을 모두 출력하게 되므로 break 필수



