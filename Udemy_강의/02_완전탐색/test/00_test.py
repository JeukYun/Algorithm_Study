# from itertools import permutations
# v = [0, 1, 2, 3]

# for i in permutations(v, 2):
#     print(i)

from itertools import combinations

v = [0, 1, 2, 3]

for i in combinations(v, 2):
    print(i)