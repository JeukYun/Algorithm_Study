import sys
input = sys.stdin.readline

n = int(input())
a = input().split()
b = input().split()

A = []
for i in a:
    A.append(int(i))

B = []
for i in b:
    B.append(int(i))


A.sort()
B.sort()
B = B[::-1]

AB = []
for a, b in zip(A, B):
    AB.append(a * b)

print(sum(AB))