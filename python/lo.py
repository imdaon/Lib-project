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


def change_password(pwd):  # 비밀번호 바꾸기
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
    print('수정완료')  
    time.sleep(1)
    os.system('clear')
    return n_pwd

def change_ID(uid):  # 아이디 변경
    n_ID = ''
    while 1:
        ID = str(input('변경할 ID입력:'))
        if ID == uid:  # 바꿀 아이디가 기본과 똑같을때
            print(f'기존과 동일한 ID 입니다.!')
            continue
        else:           # 새로운 아이디 설정
            res_ID = chk_id(ID)  # chk_ID로  조건 확인 후 res에 대입
            if not res_ID:
                continue
            else:
                n_ID = ID
                break
    print('수정완료')  
    time.sleep(1)
    os.system('clear')
    return n_ID

def change_name(name):  
    n_name = ''
    while 1:
        new_name = str(input('변경할 이름입력:'))
        if new_name == name:  
            print(f'기존과 동일한 이름 입니다.!')
            continue
        else:     
            n_name = new_name
            break    
    print('수정완료')  
    time.sleep(1)
    os.system('clear')
    return n_name

def change_num(num):  
    n_num = ''
    while 1:
        new_num = str(input('변경할 번호입력:'))
        if new_num == num:  
            print(f'기존과 동일한 번호 입니다.!')
            continue
        else:     
            n_num = new_num
            break    
    print('수정완료')  
    time.sleep(1)
    os.system('clear')
    return n_num


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
            name = input('회원가입한 이름을 입력하세요: ')
            if name in regist_id:
                print(f'아이디:{regist_id[0]}')
                print(f'비밀번호:{regist_id[1]}')

                slt = input('되돌아가기 : Q ')
                if slt == 'Q':
                    time.sleep(2)
                    os.system('clear')
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

            if (id_input ==regist_id[0]  and pw_input == regist_id[1]):
                print('로그인 성공!')
                time.sleep(1)
                os.system('clear')
            else:
                print('로그인 실패!')
                time.sleep(1)
                os.system('clear')
                continue
            
        
        elif select_no == 5: # 내정보변경
            print('1)아이디 변경 2)비밀번호 변경 3)이름 변경 4)번호 변경')
            slt = int(input('선택해주세요:'))
            if(slt == 1):
                uid = str(input('아이디를 입력해주세요:'))
                if uid in regist_id:
                    new_id=change_ID(uid)
                    regist_user[uid] = new_id
                    regist_id[0]=new_id
                    print('아이디 변경 완료\n')
                else:
                    print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                    continue
            elif(slt == 2):
                uid = str(input('아이디를 입력해주세요:'))
                if uid in regist_id:
                    new_pwd=change_password(uid)
                    regist_user[uid] = new_pwd
                    regist_id[1]=new_pwd
                    print('비밀번호 변경 완료\n')
                else:
                    print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                    continue
            elif(slt == 3):
                uid = str(input('아이디를 입력해주세요:'))
                if uid in regist_id:
                    new_name=change_name(uid)
                    regist_user[uid] = new_name
                    regist_id[2]=new_name
                    print('이름 변경 완료\n')
                else:
                    print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                    continue
            elif(slt == 4):
                uid = str(input('아이디를 입력해주세요:'))
                if uid in regist_id:
                    new_num=change_num(uid)
                    regist_user[uid] = new_num
                    regist_id[3]=new_num
                    print('번호 변경 완료\n')
                else:
                    print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                    continue
                
        elif select_no == 6:  # 종료
            sw = 0

        else:  # 예외처리
            print('잘못입력하셨습니다. 1~5 중에 골라주세요')
            time.sleep(1)
            os.system('clear')
            continue
main()