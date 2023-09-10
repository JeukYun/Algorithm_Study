# So1 
'''
map 함수 활용
    : map(function, iterable_data) 함수, 반복가능한 자료형 구조를 받아 각 자료형의 모든값에 함수를 적용

# a 정수에 1을 더하는 함수
def add(a):
    return a + 1
arr = [1, 2, 3]

# arr의 모든 요소에 add 함수를 적용하는 map 함수
add_arr = map(add, arr)
print(add_arr)
# map 객체이기 때문에 list로 반환
print(list(add_arr))

'''

# sol 1
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = input().rstrip()
E = input().rstrip()

while S in E:
    idx = E.find(S)
    for _ in range(len(S)):
        E = E[:idx] + E[idx + 1:]

if E:
    print(E)
else:
    print("EMPTY")

# sol 2
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = input().rstrip()
E = input().rstrip()

# 필터 단어 S가 메세지 E에 포함시 코드를 계속 실행
while S in E:
    # replace 메소드를 통해서 E에서 S 단어를 계속 삭제
    E = E.replace(S, '')
if E:
    print(E)
else:
    print("EMPTY")