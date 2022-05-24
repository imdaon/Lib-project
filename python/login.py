from atexit import register
import imp
from unittest import result
import re


def  make_id(regist_user):
     regist_id = []
     while 1:
         uid = str(input('회원 아이디 입력: '))
         if uid in regist_user:
             print('중복됨 ㅇㅇ')
             ex = input('메인 화면으로 이동? ㅋㅋ (y/n): ')
             if ex == 'y' or ex == 'Y':
                 return 0
             else:
                 continue
         else:
             res_id=chk_id(uid)
             if not res_id:
                 continue
             else:
                 regist_id.append(uid)
                 break    
 #print(regist_id)
     while 1:
         pwd=str(input('비번입력해라: '))
         res_pwd = chk_password(pwd)
         if not res_pwd:
             continue
         else:
             regist_id.append(pwd)
             break
         #print(regist_id)
     return regist_id

def chk_id(id):
    result = 1
    reg = r'^[A-Za-z0-9_]{4,20}$'
    if not re.search(reg, id):
        print('아이디 생성 기준에 부적당하는것이다!')
        result = 0
    return result

def chk_password(pwd):
    result = 1
    reg = r'^[A-Za-z0-9_]{4,20}$'
    #reg = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$'
    if not re.search(reg, pwd):
        print('비번 기준에 맞지 않는다는것이다!')
        result=0
    return result

def edit_password(uid, pwd):
    n_pwd = ''
    while 1:
        pw = str(input('새로운 비번 입력:'))
        if pw == pwd:
            print(f'기존 비번하고 똑같다!')
            continue
        else:
            res_pwd=chk_password(pw)
            if not res_pwd:
                continue
            else:
                n_pwd = pw
                break
    print(f'id:{uid}, n_pwd:{n_pwd}')
    return uid, n_pwd

def main():

    regist_user = {'ha':'hohoho!!11'}
    sw=1
    while sw:
        print('-'*20)
        print('1. 아이디 생성')
        print('2. 비번 번경')
        print('3. 아이디 목록 ')
        print('4. 종료')
        print('-'*20)
        select_no = int(input('번호 선택(~4): '))
        if select_no == 1:
            id_result = make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print(regist_user)
        if select_no == 2:
            uid=str(input('아이디: '))
            if uid in regist_user:
                print(f'{uid} / {regist_user[uid]}')
                n_pwd = edit_password(uid, regist_user[uid])
                regist_user[uid] = n_pwd
                print('비번번경 완료!\n')
            else:
                print('등로된 아이디가 아니라고요\n')
                continue
        if select_no == 3:
            for k, v in regist_user.items():
                print(f'id" {k} / pw: {v}')
                print()
        if select_no == 4:
            sw = 0
main()