import random

# 시작과 통계 초기화
start = 0
cnt_d = 0
cnt_w = 0
cnt_l = 0

# 게임 재시작
while start == 0:
    # 유저 가위 바위 보 입력받기
    user_rsp = input('입력해주세요 r,s,p : ').lower()
    # 유효한 값만 받기 위한 조건문
    if (user_rsp != 'r' and user_rsp != 's' and user_rsp != 'p'):
        print('유효한 입력이 아닙니다')
        continue

    # 컴퓨터 가위 바위 보 랜덤 정하기
    random_com = random.randint(1, 3)
    if (random_com == 1):
        com_rsp = 'r'
    elif (random_com == 2):
        com_rsp = 's'
    elif (random_com == 3):
        com_rsp = 'p'
    print(f'사용자: {user_rsp}, 컴퓨터: {com_rsp}')
    # 승패무 비교하기 & 출력하기
    if (com_rsp == user_rsp):
        print('무승부!')
        cnt_d += 1
    elif ((com_rsp == 'r' and user_rsp == 'p') or (com_rsp == 's' and user_rsp == 'r') or (com_rsp == 'p' and user_rsp == 's')):
        print('사용자 승리!')
        cnt_w += 1
    else:
        print('컴퓨터 승리!')
        cnt_l += 1

    # 재시작 물어보기 & 종료시 통계 출력
    while True:
        restart = input('재시작을 하시겠습니까?(y/n)').lower()
        if (restart == 'n'):
            start = 1
            print('게임을 종료합니다.')
            print(f'승 : {cnt_w} 패 : {cnt_l} 무승부 : {cnt_d}')
            break
        elif (restart == 'y'):
            start = 0
            break
        else:
            print('입력해주세요 : y or n')
            continue
