import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
num_list = []
num_dic = {}

for _ in range(N):
    n = int(input())
    num_list.append(n)

num_list = sorted(num_list)
num_set = list(set(num_list))

fq_list = []
for i in num_set:
    l = bisect_left(num_list, i)
    r = bisect_right(num_list, i)
    fq = r - l
    fq_list.append((fq, i))

fq_list = sorted(fq_list, reverse = True)

final_fq = []
if len(fq_list) == 1:
    final_fq.append(fq_list[0][1])
else:
    for i in range(len(fq_list)):
        if fq_list[0][0] <= fq_list[i][0]:
            final_fq.append(fq_list[i][1])

final_fq.sort()

print(round(sum(num_list)/len(num_list)))
print(num_list[(len(num_list)//2)])
print(final_fq[0] if len(final_fq) == 1 else final_fq[1])
print(num_list[-1] - num_list[0])