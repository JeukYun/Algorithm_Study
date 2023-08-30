# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

## 입력
user_input = input()
chr = input()
msg = input()


# 공백을 기준으로 문자 분리
num_list = user_input.split(' ')

# 처음 숫자, 나중숫자 저장
f_num = int(num_list[0])
l_num = int(num_list[1])
# 이걸 준 이유가 있을낀데....



# msg에 chr이 있는 경우 제거
if chr in msg :
	rmv = msg.replace(chr,"")
	if rmv == "" : 
		print("EMPTY")
	else:
		print(rmv)
else:
	print(msg)