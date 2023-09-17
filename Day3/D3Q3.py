## 런타임 에러 발생(코드는 맞지만 비효율적....)


# 라이브러리 호출
import numpy as np
import sys
input = sys.stdin.readline
# 입력단
array, num = map(int, input().rstrip().split(" ")) # 배열(N x N), 폭탄 수n개 입력 

# 폭탄 좌표 받기
point_list = []
for i in range(num):
    point_list.append(input())

# 배열생성
# array * array 만큼의 0으로 채워진 리스트 생성
list = [0 for i in range(array * array)] 

bomb_map = np.array(list).reshape(array, array)

# print(bomb_map)

# 폭탄좌표 주위만큼 +1 하기
# array가 3이고, 두 번째 좌표가 2,2인 경우 주변 좌표 변경


array -= 1

for i in range(len(point_list)):
    row, col = map(int, point_list[i].split(" "))
    # 좌표가 2, 2로 입력된 경우 1, 1로 변경 -> 0부터 시작하므로
    row -= 1 
    col -= 1
    # print(row,col, array)

    bomb_map[row, col] += 1 # 폭탄투하지점 +1

    if (row == 0) and (col == 0):
        bomb_map[row + 1, col] += 1 
        bomb_map[row, col + 1] += 1

    elif (row == array) & (col == array):    
        bomb_map[row - 1, col] += 1 
        bomb_map[row, col - 1] += 1 

    elif (row == 0) & (col == array):
        bomb_map[row + 1, col] += 1
        bomb_map[row, col - 1] += 1

    elif (row == array) & (col == 0):
        bomb_map[row - 1, col] += 1
        bomb_map[row, col + 1] += 1

    elif row == 0:
        bomb_map[row + 1, col] += 1 
        bomb_map[row, col + 1] += 1
        bomb_map[row, col - 1] += 1

    elif row == array:
        bomb_map[row - 1, col] += 1 
        bomb_map[row, col + 1] += 1
        bomb_map[row, col - 1] += 1

    elif col == 0:
        bomb_map[row + 1, col] += 1 
        bomb_map[row - 1, col] += 1
        bomb_map[row, col + 1] += 1

    elif col == array:
        bomb_map[row + 1, col] += 1 
        bomb_map[row - 1, col] += 1
        bomb_map[row, col - 1] += 1

    else:
        bomb_map[row + 1, col] += 1 
        bomb_map[row - 1, col] += 1
        bomb_map[row, col + 1] += 1
        bomb_map[row, col - 1] += 1
    # print(bomb_map)

print(sum(sum(bomb_map)))
