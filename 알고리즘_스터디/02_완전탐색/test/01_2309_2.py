# combinations 사용하지 않는 풀이

lst = [int(input()) for _ in range(9)]
lst.sort()
sum_lst = sum(lst)

for i in range(8):
    for k in range(i+1, 9):
        if sum_lst - lst[i] - lst[k] == 100:
            for j in range(9):
                if i != j and k != j:
                    print(lst[j])
            break
                
            