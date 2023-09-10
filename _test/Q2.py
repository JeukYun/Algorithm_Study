# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input("숫자입력")

# 처음 돈, 거래횟수 분리
inp = user_input.split(' ')
money = int(inp[0])
count = int(inp[1])


# 거래내역 pay_list에 저장
pay_list = []
for Q in range(count):
	lst = input()
	pay_list.append(lst.split(' '))

	
# reservation 대기 리스트
res_list = []


while count != 0:
	for i in range(count):
		print(i)
		M = int(pay_list[i][1]) # 추가 or 지불 금액
		R = pay_list[i][0] # 기능 (deposit or pay or reservation...)
		if R == 'deposit':
			money += M
		if R == 'pay':
			if money > M:
				money -= M
		if R == 'reservation':
			if money > M:
				money -= M
			else:
				res_list.append(M)
		print(i)
		count -= 1

		
	



	