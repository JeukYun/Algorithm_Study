#변수 입력
val1, val2, val3, val4 = map(int, input().rstrip().split(" "))
v_list = [val1, val2, val3, val4]


lst = []

for i in range(len(v_list)):
	for k in range(i+1, len(v_list)):
		lst.append(abs(v_list[i] - v_list[k]))


max_index = lst.index(max(lst))
max1_val = lst.pop(max_index)

max_index = lst.index(max(lst))
max2_val = lst.pop(max_index)

print(max1_val + max2_val)

# 오답..