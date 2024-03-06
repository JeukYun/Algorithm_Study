cache = [-1] * 91
cache[0] = 0
cache[1] = 1

'''
아래의 경우 시간초과 발생
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # 리턴값으로 재귀함수 호출...    
    return f(n-1) + f(n-2)
print(f(int(input())))
'''

def f(n):
    if cache[n] == -1:
        cache[n] = f(n-2) + f(n-1)
    return cache[n]

cache = [-1] * 91
cache[0] = 0
cache[1] = 1

# #  for문 사용시
# n = int(input())
# for i in range(2, n+1):
#     cache[i] = cache[i-1] + cache[i-2]
# print(cache[n])

print(f(int(input())))