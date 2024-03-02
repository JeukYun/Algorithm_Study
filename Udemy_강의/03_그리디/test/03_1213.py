txt = list(input())
txt.sort()

# 알파벳의 갯수를 카운트
dic = {}
for i in txt:
    dic[i] = 0
for i in txt:
    dic[i] += 1

lst = []
# 문자, 문자 갯수 리스트에 담기
for k, v in dic.items():
    lst.append((k, v))
    

palindrome = []
# 홀수개 문자 저장
not_odd = []


for i in lst:
    # 짝수개인 경우
    if not i[1] % 2:
        palindrome.append(i[0] * int(i[1]/2)) # 문자수 /2만큼 저장
    else:
        not_odd.append(i[0])
        palindrome.append(i[0] * int((i[1] - 1)/2))

# 홀수개 문자가 1개인 경우 
if len(not_odd) == 1:
    print("".join(palindrome + not_odd + palindrome[::-1])) 

# 홀수개 문자가 없는 경우
elif len(not_odd) == 0:
    print("".join(palindrome + palindrome[::-1]))

# 그 외 (홀수개 문자 2이상...)
else:
    print("I'm Sorry Hansoo")
       