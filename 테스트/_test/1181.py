import sys

N = int(input())
M_list = []
dic = {}


for i in range(N):
    M_list.append(sys.stdin.readline().rstrip()) 

M_list = sorted(M_list)

for m in M_list:
    dic[m] = len(m)

for i in range(1, 51):
    for k,v in dic.items():
        if v == i:
            print(k)