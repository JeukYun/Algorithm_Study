STR = input()


txt = ''.join(sorted(STR)) # 입력된 문자
txt_set = ''.join(sorted(set(txt))) # 중복이 제거된 문자

print(txt)
print(txt_set)

if not len(txt) % 2:
    if len(txt_set) * 2 != len(txt):
        print("I'm Sorry Hansoo")
    else:
        print(txt_set + txt_set[::-1])
else:
    if (len(txt_set)-1) * 2 != (len(txt)-1): 
        print("I'm Sorry Hansoo")
    else:
        print()

new = []
for i in range(len(txt)):
    new.append()