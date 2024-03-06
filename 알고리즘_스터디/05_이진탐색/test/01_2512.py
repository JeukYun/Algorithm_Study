import sys

N = int(input())
bugit = list(map(int, sys.stdin.readline().split()))
M = int(input())

lo, hi = 0, max(bugit)
mid = (lo + hi) // 2
ans = 0

def is_possible(mid):
    # 예산과 mid값을 비교, 작은값 반환, 
    # 반환된 값을 모두 더했을 때 예산보다 작거나 같은가?
    return sum(min(b, mid) for b in bugit) <= M


while lo <= hi:
    # mid값으로 예산배분 가능한 경우 
    if is_possible(mid):
        # low값은 mid+1
        lo = mid + 1
        # ans에 우선 mid값 저장
        ans = mid

    # mid값으로 예산배분 안되는 경우
    else:
        # high값에 mid - 1값 저장
        hi = mid - 1

    mid = (lo + hi) // 2


print(ans)

