from atexit import register
import imp
from unittest import result
import re
import os
import time


book=[['어린왕자','생택쥐베리','1'],['앨리스','루이스캐럴','2'],['소공녀','프랜시스 호지슨 버넷','3'],['아기 돼지 삼형제','조셉 제이콥스','4'],['안나 카레니나','톨스토이','5']]
bucket=[]
user_list=[[""]]
def bucket_book():
    global bookt
    global bucket
    select=""
  

    while not (select=='q' or select=='Q'):        
        print('도서 목록')
        print(book)
        select=input('장바구니에 담을 책 이름을 입력하세요 (q를 누를시 담기를 종료합니다)\n')
        for i in range(5):
            runprint = True
            if select == book[i][0]: #입력한 책이름이랑 책 리스트에 있는 책 이름이랑 같으면
                
                print(f"{book[i][0]} 장바구니에 담겼습니다")
                bucket.append(select) #입력한 책 제목을 장바구니에 추가

               
                print(f"원래 책리스트 {book}\n")
                print(f"빌린 유저 대여목록 {user_list}\n")
                print(f"장바구니 리스트 {bucket}\n")
                runprint=False
                break
            
            else:
                runprint = True
                pass
        if runprint:
            print("입력하신 책 정보가 없습니다.")

    if select == 'q' or select == 'Q':
        os.system("clear")
        print("종료합니다")
        time.sleep(1)
        os.system("clear")
        return
    
    #elif runprint:
        #print("입력하신 책 정보가 없습니다.")

def rent_book(): 
    global book
    global bucket
    select2=''
    delete2=''
    
    while(1):        
        print_taken=[]
        if not bucket==[]:
            print(f"내 장바구니 목록 {bucket}\n")  
            print(bucket)

        print('='*30)
        print('1.이전 화면으로 2.장바구니 삭제 3.대여 4.메인으로\n')
        select2=input('실행할 메뉴를 입력해주세요\n')

        if select2 == '1':
            
            print('장바구니 화면으로 돌아갑니다')
            bucket_book()
            
        if select2 == '2':
            while not (delete2=='q' or delete2=='Q'):
                delete2=input('삭제할 책 이름을 입력해주세요 종료하려면 q를\n')
                for i in range(len(bucket)):
                
                    if delete2 == bucket[i]:
                        os.system("clear")
                        print(". . . 삭제중")
                        time.sleep(1)
                        print(f"{bucket[i]} 장바구니에서 삭제 했습니다.")
                        time.sleep(1)
                        os.system("clear")
                        
                        del bucket[i]
                        
                        if not bucket==[]:
                            print(bucket)
                        break
                    else:
                        print("입력하신 책 정보가 없습니다.")
                        break

                if delete2 == 'q' or delete2 == 'Q':
                    print("종료합니다")
            
    
    
        if select2 == '3':
            print("장바구니에 있는 책을 대여합니다")
            for i in range(5):
                print("1번째")
                for j in range(len(bucket)):
                    print("2번째")
                    for k in range(len(user_list)):
                        print("3번째")
                        if bucket[j]==book[i][0] and bucket[j] != user_list[k]:
                            print("if문 들어옴?")
                            user_list.append(book[i]) #무조건 대여중으로 바뀌는 실행문보다 위에있어야함
                            book[i]=["대여중 {0}".format(bucket[j])]#"선택한 제목 이름 대여중"으로 책리스트에 추가
                            print(f"원래 책리스트 {book}\n")
                            print(f"장바구니 리스트 {bucket}\n")

                            #print("대여되었습니다")
                            
                            print(f"빌린 유저 대여목록 {user_list}\n")
                            
                            
                            #time.sleep(1)
                            #os.system("clear")
                             

                        #elif bucket[j] == user_list[k][0]:
                            #print_taken.append(bucket[j])                      
            bucket=[] #대여 하고나면 장바구니 비우기 
            print('대여되었습니다')
            print(f"최종 빌린 유저 대여목록 {user_list}\n")              
            #print(f"{print_taken}는 이미 대여되어 빌리지 못한 책입니다.")
        if select2 == '4':
            print("메인으로")
        if select2 == '5':
            return_book()

def return_book():
    global book
    global user_list
    #booksplit=[]

    turnback=''
    turnname=''
    turnnum=''

    print('    반납 방법을 선택해주세요')
    print('1.도서명으로 반납  2.도서 번호로 반납')
    turnback=input('\n')

    if turnback=='1':
       turnname=input('반납할 책 이름을 입력해주세요\n')
       for i in range(len(user_list)):
           print(f'유저대여리스트{user_list}')
           if turnname==user_list[i][0]:  #반납할 책 이름이 유저 대여 리스트에 있으면
               print(f'{turnname}반납 되었습니다')
               book.append(user_list[i])
               del user_list[i]
               for j in range(5):            
                   booksplit=book[j][0].split(' ')
                   print(f'이거맞나 : {booksplit}')
                   if(booksplit[0]=='대여중'):
                       print('들어왔니')
                       del book[j]                       
               

    if turnback=='2':
        turnnum=input('반납할 책 번호를 입력해주세요')  
        for i in range(len(user_list)):
              print(f'유저대여리스트{user_list}')
              if turnnum==user_list[i][2]:
                  print(f'{turnname}반납 되었습니다')
                  book.append(user_list[i])
                  del user_list[i]
                  for j in range(5):
                      booksplit=book[j][0].split(' ')
                      print(f'이거맞나 : {booksplit}')
                      if(booksplit[0]=='대여중'):
                          print('들어왔니')
                          del book[j]            


def make_id(regist_user):  # 아이디생성 함수
    regist_id = []   # 등록한 id 리스트
    while 1:
        uid = str(input('회원 아이디 입력: '))
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
        pwd = str(input('비번입력해라: '))
        res_pwd = chk_password(pwd)  # chk로 비번 조건 확인
        if not res_pwd:
            continue
        else:
            regist_id.append(pwd)  # 조건 만족 시 추가 (생성)

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


def edit_password(uid, pwd):  # 비밀번호 찾기
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
        print('-'*20)
        print('1. 아이디 생성(영어4글자이상)')
        print('2. 비밀번호 찾기')
        print('3. 아이디 목록 ')
        print('4. 로그인 ')
        print('5. 종료')
        print('-'*20)
        select_no = int(input('번호 선택(1~5): '))

        if select_no == 1:    # 아이디생성
            id_result = make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print('ID 생성 완료!')
                time.sleep(1)
                os.system('clear')

        elif select_no == 2:  # 비번 찾기 및 재설정
            uid = input('ID: ')
            if uid in regist_user:
                print(f'{uid} / {regist_user[uid]}')
                slt = input('되돌아가기 : Q / 재설정 : R')
                if slt == 'R':
                    n_pwd = edit_password(uid, regist_user[uid])
                    regist_user[uid] = n_pwd
                    print('비번번경 완료!\n')
                    time.sleep(1)
                    os.system('clear')
                elif slt == 'Q':
                    break
            else:
                print('등록된 ID가 아닙니다.\n')
                time.sleep(1)
                continue
        elif select_no == 3:  # 아이디 목록 확인
            for k, v in regist_user.items():
                print(f'ID: {k} / PW: {v}')
                time.sleep(1)
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
            bucket_book()
            rent_book() 
        elif select_no == 5:  # 종료
            sw = 0

        else:  # 예외처리
            print('잘못입력하셨습니다. 1~5 중에 골라주세요')
            time.sleep(1)
            os.system('clear')
            continue


main()