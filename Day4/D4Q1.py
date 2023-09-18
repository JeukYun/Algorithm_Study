inp_num = int(input())
pwd = list(input())

# 알파벳은 26개 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

raw = []

# 암호에서 숫자만 추출
num = list(map(int, pwd[1::2]))
str_pwd = pwd[0::2]
# print(num)
# print(str_pwd)
# print(alphabet.index(str_pwd[0]))

for i in range(len(num)):
    square_num = num[i] * num[i]
    if square_num < 26:
        idx_num = square_num
    else:
        idx_num = square_num % 26
    al_idx = alphabet.index(str_pwd[i])
    index = (square_num + al_idx) % 26
    
    raw.append(alphabet[index])

print("".join(raw))

