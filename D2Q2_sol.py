'''
2진수 변환 코드

A = int(input())
result = []
while A:
    result.append(str(A % 2))
    A //= 2  # 2로 나눈 몫을 A에 할당
print(''.join(reversed(result))) # 리스트의 요소를 문자열과 결합 ''과 함께 사용시 문자열만 나열

'''


# sol
import sys
input = sys.stdin.readline

N = int(input())
# 배열로 모든 정수를 입력.
S = list(map(int, input().split()))

# 모든 정수를 더한 후에, 8진수 변환
print(oct(sum(S))[2:])


# bin : 10진수 -> 2진수 변환 (접두사 0b)
# oct : 10진수 -> 8진수로 변환 (접두사 0o)
# hex : 10진수 -> 18진수 변환 (접두사 0x)