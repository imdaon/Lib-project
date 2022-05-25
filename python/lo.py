from atexit import register
import imp
from unittest import result
import re
import os
import time

regist_id = []   # 등록한 id 리스트

def make_id(regist_user):  # 아이디생성 함수
    
    while 1:
        uid = str(input('아이디를 입력하세요: '))
        if uid in regist_user:  # 아이디 중복 확인
            print('중복됨 ㅇㅇ')
            ex = input('메인 화면으로 이동? ㅋㅋ (y/n): ')
            if ex == 'y' or ex == 'Y':
                return 0
            else:
                continue
        else:  # 아이디 중복 아닐 시
            res_id = chk_id(uid)
            if not res_id:
                continue
            else:
                regist_id.append(uid)  # append로 리스트에 추가
                break

    while 1:
        pwd = str(input('비밀번호를 입력하세요: '))
        res_pwd = chk_password(pwd)  # chk로 비번 조건 확인
        if not res_pwd:
            continue
        else:
            regist_id.append(pwd)  # 조건 만족 시 추가 (생성)
            break

    while 1:
        name = str(input('이름을 입력하세요: '))
        if not name:
            continue
        else:
            regist_id.append(name)  # 조건 만족 시 추가 (생성)
            break
    while 1:
        num = str(input('번호를 입력하세요: '))
        if not num:
            continue
        else:
            regist_id.append(num)  # 조건 만족 시 추가 (생성)
            break

    return regist_id


def chk_id(id):  # ID만들때 조건  영어&숫자 4글자 이상
    result = 1
    reg = r'^[A-Za-z0-9_]{4,20}$'
    if not re.search(reg, id):
        print('아이디 생성 기준에 부적당하는것이다!')
        result = 0
    return result


def chk_password(pwd):  # 비번만들때 조건 영어&숫자 4글자 이상
    result = 1
    reg = r'^[A-Za-z0-9_]{4,20}$'
    # reg = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$' --> 이건 대,소문자 + 특수문자 포함
    if not re.search(reg, pwd):
        print('비번 기준에 맞지 않는다는것이다!')
        result = 0
    return result


def change_password(uid, pwd):  # 비밀번호 찾기
    n_pwd = ''
    while 1:
        pw = str(input('새로운 비번 입력:'))
        if pw == pwd:  # 바꿀 비번이 기본과 똑같을때
            print(f'기존의 비밀번호 입니다.!')
            continue
        else:           # 새로운 비밀번호 설정
            res_pwd = chk_password(pw)  # chk_pas로 비번 조건 확인 후 res에 대입
            if not res_pwd:
                continue
            else:
                n_pwd = pw
                break
    print(f'id:{uid}, n_pwd:{n_pwd}')   # 새로운 비밀번호 및 아이디 확인
    return n_pwd


def main():

    regist_user = {}    # regist_user 딕셔너리 (만든 아이디 저장)
    sw = 1  # while문 1 or 0 조건을 위해 선언
    while sw:
        print('-'*30)
        print('1. 아이디 생성(영어4글자이상)')
        print('2. 아이디 & 비밀번호 찾기')
        print('3. 아이디 목록 ')
        print('4. 로그인 ')
        print('5. 내정보 변경')
        print('6. 종료')
        print('-'*30)
        select_no = int(input('번호 선택(1~5): '))

        if select_no == 1:    # 아이디생성
            id_result = make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print('ID 생성 완료!')
                time.sleep(1)
                os.system('clear')

        elif select_no == 2:  # ID/PW 찾기
            name = input('개인정보 아무거나 입력하세요: ')
            if name in regist_id:
                regist_num=regist_id.index(name)
                print(f'이름:{regist_id[regist_num]}')
                print(f'아이디:{regist_id[regist_num-2]}')
                print(f'비밀번호:{regist_id[regist_num-1]}')

                slt = input('되돌아가기 : Q ')
                if slt == 'Q':
                    break
            else:
                print('등록된 ID가 아닙니다.\n')
                time.sleep(1)
                continue
        elif select_no == 3:  # 아이디 목록 확인
            for i in regist_id:
                print(i)
            time.sleep(2)
            os.system('clear')

        elif select_no == 4:  # 로그인
            id_input = input('ID 입력:')
            pw_input = input('PW 입력:')
            for i, j in regist_user.items():  # items 로 아이디,비번 각각 확인 후 비교
                if (id_input == f'{i}' and pw_input == f'{j}') == False:
                    print('로그인 실패!')
                else:
                    print('로그인 성공!')
                    continue
            time.sleep(1)
            os.system('clear')
        elif select_no == 5:  # 비번 찾기 및 재설정
            uid = input('아이디: ')
            if uid in regist_user:
                print(f'{uid} / {regist_user[uid]}')
                n_pwd = edit_password(uid, regist_user[uid])
                regist_user[uid] = n_pwd
                print('비번번경 완료!\n')
                time.sleep(2)
                os.system('clear')
            else:
                print('등로된 아이디가 아니라고요\n')
                continue

        elif select_no == 6:  # 종료
            sw = 0

        else:  # 예외처리
            print('잘못입력하셨습니다. 1~5 중에 골라주세요')
            time.sleep(1)
            os.system('clear')
            continue
main()