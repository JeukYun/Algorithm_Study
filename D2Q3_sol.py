# sol

import sys
input = sys.stdin.readline

def Sieve(N):
    is_prime = [1 for _ in range(N + 1)]
    prime = []
    for i in range(2, N + 1):
        if not is_prime[i]:
            continue
        prime.append(i)
        for j in range(2 * i, N + 1, i):
            is_prime[j] = 0
    return prime

N = int(input())
A = [0] + list(map(int, input().split()))
ans = 0

primes = Sieve(N)
for prime in primes:
    ans += A[prime]
        
print(ans)