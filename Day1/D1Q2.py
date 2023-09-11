# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 입력
len_N = input()
Word = input()
Mess = input()


# 입력받은 len_N을 공백을 기준으로 분리, 변수에 저장
len_danger, len_total = len_N.split(" ") 

len_danger = int(len_danger)
len_total = int(len_total) 


# 반복문 작성
while Word in Mess: # Mess에 Word가 포함 되어 있는 동안 아래를 계속 실행
	# 1. Mess에 Word 포함 시 Word를 빈문자로 치환
	if Word in Mess: 
		Mess = Mess.replace(Word,"")
	# 2. Mess에 아무것도 안남은 경우 Mess = EMPTY
	if Mess == "":
		Mess = "EMPTY"
	
print(Mess)
	

# 정답