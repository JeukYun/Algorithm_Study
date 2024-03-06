import random

num = input()
num_list = list(map(int,input().split()))
print(num_list)

for i in range(len(num)):
    a = random.choice(num_list)
    b = random.choice(num_list)
    if a == b:
        continue
    c = random.choice(num_list)
    if b == c:
        continue
    

