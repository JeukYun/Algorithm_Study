from itertools import combinations

lst = []

for _ in range(9):
    lst.append(int(input()))


sum_lst = []
for _ in combinations(lst, 7):
    sum_lst.append(_)

for lst in sum_lst:
    if sum(lst) == 100:
        lst = list(lst)
        lst.sort(reverse = True)
        # print(lst)
        break

for _ in range(len(lst)):
    # print(lst)
    print(lst.pop())


