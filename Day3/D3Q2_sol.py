answer = list(map(int, input()))
user_input = list(map(int, input()))

def fail():
    for i in range(4):
        if result[i] == 2:
            # 결과가 fail인 경우 아래 반복문 실행
            while True:
                # 해당 값에 1을 더한 후 10으로 나눈 나머지 : temp에 저장
                temp = (user_input[i] + 1) % 10
                out = temp not in user_input
                user_input[i] = temp
                if out:
                    break

def ball():
    if 1 not in result: # result에 1(ball)이 없는경우 건너뜀 
        return
    pos = [] # 1이 있는 위치 : pos
    value = [] # 1에 해당하는 값 : value
    for i in range(4):
        if result[i] != 0: # result의 i번째가 0(strike)이 아닌 경우 아래 문장 실행 
            pos.append(i) # 1(ball)에 해당되는 위치 pos에 저장
            value.append(user_input[i]) # 1에 해당하는 값 value에 저장
    for i in range(len(pos)): # 1인 갯수만큼 반복
        if i == 0:
            user_input[pos[i]] = value[-1] # pos의 0번째 해당하는 위치의 input값을 value의 마지막 값으로 치환
        else:
            user_input[pos[i]] = value[i - 1] # pos의 i번째 해당하는 위치의 input값을 value의 i-1 값으로 치환

make_input_count = 0
while True:
    make_input_count += 1
    result = [2, 2, 2, 2]
    # 초기 결과값을 저장하는 리스트 생성
    # strike : 0 / ball : 1 / fail : 2
    # 초기값은 모두 2(fail)
    if user_input == answer:
        # 입력과 정답이 일치하는 경우 반복문 탈출(break)
        print(make_input_count)
        break

    for i in range(4):
        if user_input[i] in answer:
            # 입력값의 1~4번째 돌아가며 정답에 포함 여부 확인
            if user_input[i] == answer[i]:
                # 자리까지 동일 한 경우
                result[i] = 0
                # 해당 result의 자리 0(strike)으로 변경
            else:
                #자리는 일치하지 않은 경우 1(ball)으로 변경
                result[i] = 1
                
                
    fail()
    ball()
