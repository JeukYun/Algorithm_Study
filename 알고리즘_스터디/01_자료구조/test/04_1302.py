import sys

d= {}

n = int(sys.stdin.readline())

for _ in range(n):
    book = sys.stdin.readline().rstrip()

    if book in d:
        d[book] += 1
    else:
        d[book] = 1

max_val = max(d.values())

max_b = []

for k,v in d.items():
    # print(k, v)
    if v == max_val:
        max_b.append(k)

print(sorted(max_b)[0])