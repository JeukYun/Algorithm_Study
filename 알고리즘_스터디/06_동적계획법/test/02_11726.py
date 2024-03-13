cache = [-1] * 1001
cache[0] = 0
cache[1] = 1
cache[2] = 2
cache[3] = 3

def f(n):
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]

print(f(int(input())) % 10007)