# 입력단
n_count = int(input())
num_list = list(map(int, input().rstrip().split(" ")))

print(num_list)

'''
소수 : 1보다 큰 자연수 중 1과 자기 자신을 제외한 값 외에 나누어 떨어지지 않는 수
1은 소수가 아님.
'''

def is_sosu(x):
	if x < 2: # 1은 소수가 아니므로 1보다 커야함
		return 
	if (x > 2) & (x % 2 == 0): # 2로 나누어 떨어지는 수 (2의배수)는 소수가 아님.
		return 
	if (x > 3) & (x % 3 == 0): # 3으로 나누어 떨어지는 수는 소수 x
		return
	if (x > 5) & (x % 5 == 0):
		return 
	if (x > 7) & (x % 7 == 0):
		return
	else:
		return x
	
sosu = list(map(is_sosu, num_list))

print(sosu)

# 오답..