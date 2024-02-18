N, L = map(int, input().split()) # 테이프 개수, 길이


# 구멍이 난 곳 좌표 입력을 위해 1001개의 구간 생성
coord = [False] * 1001 # 인덱스 0~1000까지 받기 위해 1001생성


# 좌표값을 입력받아 좌표에 해당하는 경우 True로 변경
for i in map(int, input().split()):
    coord[i] = True


ans = 0
x = 0

while x < 1001:
    if coord[x]: # 좌표값 True(구멍)인 경우
        ans += 1 # 사용한 테이프 +1
        x += L   # 테이프 길이만큼 좌표 건너뛰기
    else:
        x += 1
        
print(ans)
