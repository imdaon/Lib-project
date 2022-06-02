import imp
import os
import re
from re import T
from atexit import register
#from tkinter.tix import Select
from unittest import result
import time
import random
import sqlite3

#test주석
#데이터 베이스 연결 
#conn=sqlite3.connect("lib_project",isolation_level=None)
#cur=conn.cursor()
#cur.execute("SELECT * FROM booklist")
#print(cur.fetchall())


book=[]
bucket=[]
user_list=[["","",""]]
myBook=['삼국지', '조선왕조실록', '이순신의 바다'] #소유한 책
returninfo=[]
regist_id = []   # 등록한 id 리스트
userid=''


def bucket_book():  #장바구니
    global bookt1
    global bucket
    select=""
    
    conn=sqlite3.connect("lib_project")
    cur=conn.cursor()

    if not bucket==[]:
            print(f"내 장바구니 목록 ₍ ᐢ. ̫ .ᐢ ₎ . . {bucket}\n")
    print('')

    select=input('장바구니에 담을 책 이름을 입력하세요 (q를 누를시 담기를 종료합니다)\n')
    find=cur.execute('SELECT bookname from rentlist where bookname=?',(select,))
    find=find.fetchone()  

    if find is None:
        print('대여가능')
        select = '%' + select + '%'
        cur.execute('SELECT bookname,booknum from booklist where bookname like ?',(select,))
        result=cur.fetchall()
        print('')
        print(*result, sep='\n') #이쁘게 나옴
        
        bookselect=input('대여할 책의 번호를 입력해주세요')
        #입력한 책이 책 리스트에 있는지 검사 
        find=cur.execute('SELECT booknum,bookname from booklist where booknum=?',(bookselect,))
        find=find.fetchone()

        if find is None:
            print('그런책없음')
        else:
            #대여리스트에 있는지 검사 
            find2=cur.execute('SELECT booknum,bookname from rentlist where booknum=?',(bookselect,))
            find2=find2.fetchone()
            #대여 리스트에 없으면 
            if find2 is None:
                bucket.append(find)
                print('=====================₍ ᐢ. ̫ .ᐢ ₎==================')
                print(f"장바구니 리스트 {bucket}\n")
                print('===============================================')  
            else:
                print('error 이미 대여중인 책입니다')
                time.sleep(2)             

    else:
        print('이미 대여중인 책입니다')


    if select == 'q' or select == 'Q':
        os.system("clear")
        print("종료합니다")
        time.sleep(1)
        os.system("clear")
    conn.close()
    rent_book()    
    
def rent_book(): #대여
    global book
    global bucket
    select2=''
    rent=''
    
    time.sleep(1)
    os.system("clear")

    while(1):        
        if not bucket==[]:
            print(f"내 장바구니 목록 ₍ ᐢ. ̫ .ᐢ ₎ . . {bucket}\n")  
         

        print('='*55)
        print('1.장바구니담기 2.대여 3.메인으로 4.반납\n')
        select2=input()

        if select2 == '1':
            
            print('장바구니 화면으로 돌아갑니다')
            time.sleep(1)
            os.system('clear')
            bucket_book()            
    
        if select2 == '2': #대여
            
            conn=sqlite3.connect("lib_project")
            cur=conn.cursor()
    
            print('')
            print('=====================₍ ᐢ. ̫ .ᐢ ₎==================')
            print(f"장바구니 리스트 {bucket}",sep='\n')
            print('===============================================')              

            #userid=input('id를 입력하세요: ')
            bookselect=input('대여할 책의 번호를 입력해주세요: ')
            rentBool=True
            for i in bucket:
                if bookselect == str(i[0]):
                    find=cur.execute('SELECT booknum,bookname,writer from booklist where booknum=?',(bookselect,))
                    find=find.fetchone()
                   
                    if find is None:
                        print('입력 정보를 다시 확인 해주세요')
                    else:
                        cur.execute("SELECT rentcount FROM userlist WHERE userid=?",(userid,)) #입력한 아이디의 행 수를 count
                        count=cur.fetchone()
                        print(f'{count[0]}가뭐임')
                        if count[0]>=3:
                            print('최대 대여 권수를 초과했습니다')
                            rentBool=False
                            time.sleep(1)
                        else:        
                            rentBool=False                            
                            print('')
                            print(' 대여 완료 ^ㅅ^)b ')
                            cur.execute("INSERT INTO rentlist VALUES(?,?,?,?,date('now'),date('now','7 days'))",(find[0],find[1],find[2],userid))
                            cur.execute("UPDATE userlist SET rentcount=rentcount+1 WHERE userid=?",(userid,))
                            conn.commit()
                            conn.close()
                            
                            for i in bucket:
                                if str(i[0])==bookselect:
                                    num=bucket.index(i)
                                    del bucket[num]
                                    #print(f"장바구니 리스트 {bucket}",sep='\n')                               
            if(rentBool):
                print('error 1004 입력 정보를 확인해주세요 ')
                    #time.sleep(1)
                    #os.system('clear')  

        if select2 == '3':
            main()
        if select2 == '4':
            return_book()
    


def return_book():
    global book
    global user_list
    turnback=''
    turnname=''
    turnnum=''
    conn=sqlite3.connect("lib_project")
    cur=conn.cursor()

    print('    반납 방법을 선택해주세요')
    print('1.도서명으로 반납  2.도서 번호로 반납')
    turnback=input('\n')

    if turnback=='1':
        #userid=input('아이디를 입력해주세요')
        turnname=input('반납할 책 이름을 입력해주세요: ')
        cur.execute('SELECT booknum,bookname,userid,date from rentlist where bookname=?',(turnname,))
        find=(cur.fetchone())

        if find is None:
            print('error 입력 정보를 확인해주세요')

        else:

            cur.execute('DELETE from rentlist where bookname=?',(turnname,))
            conn.commit()
            cur.execute("INSERT INTO returnlist VALUES(?,?,?,?,date('now'))",(find[0],find[1],find[2],find[3]))
            cur.execute("UPDATE userlist SET rentcount=rentcount-1 WHERE userid=?",(userid,))
            conn.commit()
            conn.close()
            os.system("clear")
            time.sleep(1)
            print(f'{find[0],find[1]} 반납 되었습니다 ᴖ-ᴖ')
    
                        
    if turnback=='2':
        #userid=input('아이디를 입력해주세요')
        turnnum=input('반납할 책 번호를 입력해주세요')
        cur.execute('SELECT booknum,bookname,userid,date from rentlist where booknum=?',(turnnum,))
        find=(cur.fetchone())
        print(f'find가 뭐야? {find}' )

        if find is None:
            print('error 입력 정보를 확인해주세요')

        else:

            cur.execute('DELETE from rentlist where booknum=?',(turnnum,))
            conn.commit()
            cur.execute("INSERT INTO returnlist VALUES(?,?,?,?,date('now'))",(find[0],find[1],find[2],find[3]))
            cur.execute("UPDATE userlist SET rentcount=rentcount-1 WHERE userid=?",(userid,))
            conn.commit()
            conn.close()
            os.system("clear")
            time.sleep(1)
            print(f'{find[0],find[1]} 반납 되었습니다 ᴖ-ᴖ')
'''
def SearchBar(): #조회
    while 1:
        find = input('-'*3+'도서 자료를 입력해 주세요'+'-'*3+'\n'+'(고유번호/책이름/저자)(종료:나가기): ')
        
        #이렇게 하니까 꼭 정확하게 입력 해야만 뜸
        #cur.execute("SELECT * FROM booklist WHERE booknum=? OR bookname=? OR writer=? ",(find,find,find)) #인수 무조건 튜플이나 리스트로 묶어서 줘야함.
        
        find = '%' + find + '%' #find 앞뒤로 문자열이 붙어도 상관 없다는 의미. 꼭 붙여줘야함
        cur.execute("SELECT * FROM booklist WHERE bookname like ?",(find,))
        cur.execute("SELECT * FROM booklist WHERE writer like ?",(find,)) #인수 무조건 튜플이나 리스트로 묶어서 줘야함.
        Result= cur.fetchall()  #result[0]=booknum result[1]=bookname result[2]=writer   
        
        print('')
        print(*Result, sep='\n') #정갈하게 나온다!!! 
        #print('책이름:' ,Result[1],'저자',Result[2]) #이렇게 쓸거면 fetchall()쓰면 안됨 fetchone 해서 하나씩 출력해야함 
        
        if find == '나가기':
            print('검색을 종료 합니다')
            time.sleep(1)
            os.system("clear")
            return
'''
def Recommend(): #추천 도서
    booklen=len(book)
    print('-'*5+'추천 도서'+'-'*5)
    for i in random.sample(range(booklen), 3): #도서 리스트 추가시 자동 적용
        print(f'{book[i][0]:>10}')
    print('-' *19)
   
'''
def Donation(): #기증
    bookcnt=len(book)+1 # 0부터 시작이므로 +1
    print('-'*13+'소유한 책 리스트'+'-'*13)
    print(f'{myBook}'+'\n')

    donate = input("'기증' 하시겠습니까?(Y/n)")
    if donate == 'Y' or donate == 'y':
        while 1:
            bookname = input("도서 명: ")
            writer = input("저자: ")
            if bookname not in myBook: #소유 책, 기증 명 불 일치 시
                print("소유한 '도서 명' 다릅니다. 다시 입력 하세요")
                return Donation()                
            else: #일치 시
                book.append([f'{bookname}', f'{writer}', f'{str(bookcnt)}']) #고유번호 문자로 변환
                myBook.remove(bookname)
                print('"'+bookname+'"기증 완료 되었습니다')
                bookcnt +=1
                return Donation()
    elif donate == 'N' or donate == 'n':
        print('기증을 취소합니다')
        return
    else :
        print('다시 입력하세요')
        return Donation()
'''


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
    global returninfo
    menu_select=''
    slt=''
    conn=sqlite3.connect("lib_project")
    cur=conn.cursor()

    os.system("clear")
    while(1):
        #time.sleep(1)
        #os.system("clear")
        
       # Recommend() #추천 도서 함수

        print('1.조회 2.대여 3.반납 4.기증 5.나의정보')
        menu_select=input()
        
       # if(menu_select=='1'):
       #     SearchBar() #도서 검색 함수
        if(menu_select=='2'):
            bucket_book() #대여/장바구니 함수
        if(menu_select=='3'):
            return_book() #반납 함수 
       # if(menu_select=='4'):
       #     Donation() #기증 함수
        if(menu_select=='5'):
            while (1):
                os.system("clear")
                time.sleep(1)
                #userid=input('아이디를 입력해주세요')
                print('---------ଘʕ੭·ㅅ·ʔ੭ 내 정보 ଘʕ੭·ㅅ·ʔ੭---------')

                print('▶ 대여중인 도서 리스트')
                #if not user_list==[]:
                    #print(user_list)    
                cur.execute('SELECT * FROM rentlist WHERE userid=?',(userid,))
                find=cur.fetchall()
                print(find)
                
                print('='*30)
                print('▶ 대여후 반납한 도서 리스트')
                #if not returninfo==[]:
                    #print(returninfo)
                cur.execute('SELECT * FROM returnlist WHERE userid=?',(userid,))
                find=cur.fetchall()
                print(find)    
                
                print('▶ 미납중인 도서 리스트')
                #if not user_list==[]:
                    #print(user_list)
                cur.execute('SELECT * FROM rentlist WHERE userid=?',(userid,))
                find=cur.fetchall()
                print(find)    
                        
                print('='*30)

                print('1.내 정보 변경')
                print('2.연체 정보 조회하기')
                print('-----------------------------------------') 
                slt=input()
                if slt=='1':  #내 정보 변경
                    regist_user = {}    # regist_user 딕셔너리 (만든 아이디 저장)
                    sw = 1  
                    while sw:
                        print('1)아이디 변경 2)비밀번호 변경 3)이름 변경 4)번호 변경')
                        slt = input('선택해주세요:')
                        if(slt == '1'):
                            uid = str(input('아이디를 입력해주세요:'))
                            if uid in regist_id:
                                new_id=change_ID(uid)
                                regist_user[uid] = new_id
                                regist_id[0]=new_id
                                print('아이디 변경 완료\n')
                            else:
                                print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                                continue
                        elif(slt == '2'):
                            uid = str(input('아이디를 입력해주세요:'))
                            if uid in regist_id:
                                new_pwd=change_password(uid)
                                regist_user[uid] = new_pwd
                                regist_id[1]=new_pwd
                                print('비밀번호 변경 완료\n')
                            else:
                                print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                                continue
                        elif(slt == '3'):
                            uid = str(input('아이디를 입력해주세요:'))
                            if uid in regist_id:
                                new_name=change_name(uid)
                                regist_user[uid] = new_name
                                regist_id[2]=new_name
                                print('이름 변경 완료\n')
                            else:
                                print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                                continue
                        elif(slt == '4'):
                            uid = str(input('아이디를 입력해주세요:'))
                            if uid in regist_id:
                                new_num=change_num(uid)
                                regist_user[uid] = new_num
                                regist_id[3]=new_num
                                print('번호 변경 완료\n')
                            else:
                                print('등록되어 있지 않은 아이디입니다. 아이디를 확인해주세요\n')
                                continue
                        elif(slt=='q'or slt=='ㅂ'):
                            break        
                    else:  # 예외처리
                        print('잘못입력하셨습니다. 1~5 중에 골라주세요')
                        time.sleep(1)
                        os.system('clear')
                        continue
                            
                if slt=='2':
                    print('연체 정보 없음')
                    cur.execute("SELECT bookname,writer,returndate FROM rentlist WHERE userid=?",(userid,))
                    find=cur.fetchall()
                    for i in find:
                        print(f'{i[0]},{i[1]}, 반납일은 {i[2]}까지 입니다.')

                    
                
                if slt=='q'or'ㅂ':
                    break
      
def main2():

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
                global userid
                userid=id_input
                main()
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
main2()