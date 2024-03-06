import sys

n = int(sys.stdin.readline())

for i in range(n):
    VPS = sys.stdin.readline().rstrip()
    if len(VPS) == 0:
        print("NO")
        break

    ISVPS = []
    for ps in VPS:
        if ps == '(':
            ISVPS.append(ps)
        elif ps == ')' :
            if len(ISVPS) == 0:
                ISVPS.append(ps)
                break

            elif ISVPS[-1] == '(':
                ISVPS.pop()

            else:
                ISVPS.append(ps)
    
    if len(ISVPS) == 0:
        print('YES')
    else:
        print('NO') 

