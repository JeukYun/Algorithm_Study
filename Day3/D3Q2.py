answer = list(map(int, input()))
user_input = list(map(int, input()))
# 사용자 입력을 만든 횟수
make_input_count = 0


# fail인 경우 함수 생성
def fail():
    for i in range(4):
        # result의 결과가 fail(2)인경우 실행
        if result[i] == 2: # fail인 경우
            while True:
                temp = (user_input[i] + 1) % 10 # 입력값 +1 % 10
                if temp not in user_input:
                    user_input[i] = temp
                    break


# ball인 경우 함수 생성
def ball():
    if 1 not in result:
        return
    pos = []
    val = []
    for i in range(4):
        if result[i] != 0:
            pos.append(i)
            val.append(user_input[i])
    for i in range(len(pos)):
        if i == 0:
            user_input[pos[i]] = val[-1]
        else:
            user_input[pos[i]] = val[i -1]
            


while True:
    make_input_count += 1
    # result : 0 = strike, 1 = ball, 2 = fail
    # 초기 result값은 2(fail)로 설정
    result = [2, 2, 2, 2]

    # 정답과 user의 입력값이 동일 : 승리
    if answer == user_input:
        print(make_input_count)
        break # 승리 시 반복문을 빠져나옴.

    # 정답, user입력이 다른 경우
    for i in range(4):
        # 입력값이 정답에 포함되는경우
        if user_input[i] in answer: 
            # 자리까지 일치하는 경우
            if user_input[i] == answer[i]:
                result[i] == 0 # 해당 자리의 result를 0(strike)
            # 자리는 일치하지 않는 경우
            else:
                result[i] == 1 # 해당 자리의 result를 1(ball)
    
    fail()
    ball()