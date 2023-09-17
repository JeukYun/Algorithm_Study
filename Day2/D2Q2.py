# 입력단
count_n = int(input())
n_lst = list(map(int, input().rstrip().split(" ")))


# 주어진 값 합계를 구하기
sum_n = 0

for i in range(count_n):
	sum_n += n_lst[i]


# 값 합계를 8로 나눈 나머지들 저장
mod_list = []

while sum_n > 8:
	n1 = sum_n // 8
	n2 = sum_n % 8

	mod_list.append(n2)
	sum_n = n1

mod_list.append(n1) # 마지막의 8미만 값 list에 추가


# 처음 저장 된 값이 마지막에 나오게
new_list = mod_list[::-1]

# list에 저장 된 값을 빼서 int형으로 변환
str_num = ""
for i in range(len(new_list)):
	str_num += str(new_list[i])

num = int(str_num)
print(num)


# 정답