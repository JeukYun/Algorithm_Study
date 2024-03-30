import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
lst = [1, 5, 10, 50]
num_set = set()


for comb in combinations_with_replacement(lst, N):
    num_set.add(sum(comb))

print(len(num_set))