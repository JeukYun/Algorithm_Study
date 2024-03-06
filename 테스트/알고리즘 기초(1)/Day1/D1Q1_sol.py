'''
다량의 문자를 읽어들이는 상황에서는 input()함수가 불리.
다량의 문자 읽는 경우 sys.stdin.readline()함수 지향
'''

# Sol 1
import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()
result = ''

for i in S:
	if i.islower():
		result += i.upper()
	elif i.isupper():
		result += i.lower()
print(result)


#############################

# Sol 2
import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()
print(S.swapcase())


