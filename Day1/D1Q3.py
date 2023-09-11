# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
formula = input()

f1, f2 = formula.split(" ")



## eval 쓰면 안좋다 해서 + - * 구현할랬는데 포기....

# cal_list = ["+", "-", "*"]
# cal_in = []

# def rmv_chr(x):
# 	for cal in cal_list:
# 		while cal in x:
# 			if "+" in x:
# 				x = x.replace("+", " ")
# 			if "-" in x:
# 				x = x.replace("-", " ")
# 			if "*" in x:
# 				x = x.replace("*", " ")
# 		cal_in.append(cal)
# 	return x.split(" ")

# f1_s = rmv_chr(f1)
# f2_s = rmv_chr(f2)

# def calcul(f,cal):
# 	result = 0
# 	if cal.pop() == "+":
		

if eval(f1) > eval(f2):
	print(eval(f1))
else:
	print(eval(f2))


# 정답