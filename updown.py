import random

#시작과 최고기록 초기화
start=0
max_cnt=0

#게임 재시작
while start==0:
    random_com=random.randint(1,100)
    cnt=0
    #한게임 시작
    while True: 
        try:
            #예측 숫자 입력받고 횟수증가
            user_number=int(input('숫자를 입력해주세요(1~100) : '))
            cnt+=1
            #비교 후 힌트 혹은 최종 횟수 출력 & 유효범위 제한
            if(random_com==user_number):
                print('맞춰버렸네 까비')
                print(f'최종 횟수 : {cnt}')
                break
            elif(random_com<user_number and 1<=user_number<=100):
                print('다운')
                continue
            elif(random_com>user_number and 1<=user_number<=100):
                print('업')
                continue
            elif(user_number>100 or user_number<1):
                print('유효한 범위 내의 숫자 입력해주세요(1~100)')
                cnt-=1
                continue
        except ValueError :
            print('유효한 범위 내의 숫자 입력해주세요(1~100)')

    #오래 걸린 기록 체크
    if(max_cnt<cnt):
        max_cnt=cnt
    else:
        max_cnt=max_cnt

    #재시작 물어보기 & 다시 시작시 최고 오래걸린 기록 출력
    while True:
        restart=input('재시작을 하시겠습니까?(y/n)').lower()
        if(restart=='n'):
            start=1
            print('게임을 종료합니다.')
            break
        elif(restart=='y'):
            start=0
            print('새게임')
            print(f'최고 횟수 : {max_cnt}')
            break
        else:
            print('입력해주세요 : y or n')
            continue