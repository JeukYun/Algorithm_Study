import sys

num, val = map(int, input().split())

val_list = []

for _ in range(num):
    val_list.append(int(sys.stdin.readline()))


count = 0

for k in reversed(val_list):  
    if k <= val:
        count += val // k
        val = val % k

        # if val == 0:
            # break
        
print(count)
