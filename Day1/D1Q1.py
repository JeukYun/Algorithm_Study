# 문제 : 입력2 의 문자를 대문자를 소문자/ 소문자를 대문자로 변경하여 출력
# 입력 1. 문자열 길이
# 입력 2. 문자
# 출력 : 대소문자 변경



# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 입력
len_S = int(input()) # 문자열 -> int형 변환
String = input()

# 빈 문자열 생성
new_string = ""


# 글자 수 만큼 for문 생성
for i in range(len_S):
	S = String[i]		# String의 첫 문자를 S 변수에 저장
	if S.islower(): 
		new_string += S.upper()	# S가 소문자가 참이면 대문자 변환 후 new_string에 삽입
	if S.isupper():
		new_string += S.lower() # S가 대문자가 참이면 소문자 변환 후 new_string에 삽입
		
print(new_string)