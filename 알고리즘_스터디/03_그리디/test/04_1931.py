import sys
input = sys.stdin.readline

N = int(input())
t_lst = []

for _ in range(N):
    s,e = map(int, input().split())
    t_lst.append((s,e))
t_lst.sort(key = lambda x : (x[1], x[0]))

# print(t_lst)

END = t_lst[0][1]
# print(END)
count = 1

for i in range(1, len(t_lst)):
    if t_lst[i][0] >= END:
        END = t_lst[i][1]
        count += 1

print(count)