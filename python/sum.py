from ast import Num
import os
import re
from re import T
from atexit import register
from unittest import result
import time
import sqlite3
from unittest import result

book = [['어린왕자', '생택쥐베리', '1'], ['앨리스', '루이스캐럴', '2'], ['소공녀', '프랜시스 호지슨 버넷', '3'], ['아기돼지삼형제', '조셉 제이콥스', '4'],
        ['안나카레니나', '톨스토이', '5']]
bucket = []
user_list = [["", "", ""]]
myBook = ['삼국지', '조선왕조실록', '이순신의 바다']  # 소유한 책
returninfo = []
regist_id = []  # 등록한 id 리스트
conn = sqlite3.connect("lib_project", isolation_level=None)  # 데이터베이스 연결
c = conn.cursor()  # 커서생성
c.execute("SELECT id,pwd FROM userlist")  # 로그인할때 필요한 id,pwd읽기
db_user = c.fetchall()  # 동일함
UserID=''
uid = ''
pwd = ''
name = ''
num = ''


def bucket_book():
    global bookt
    global bucket
    select = ""

    while not (select == 'q' or select == 'Q'):
        print('                              <도서 목록>')
        print('\n')
        print(book)
        print('\n')
        select = input('장바구니에 담을 책 이름을 입력하세요 (q를 누를시 담기를 종료합니다)\n')
        os.system("clear")
        for i in range(5):
            runprint = True
            if select == book[i][0]:  # 입력한 책이름이랑 책 리스트에 있는 책 이름이랑 같으면
                print(f"{book[i][0]} 장바구니에 담겼습니다!")
                time.sleep(1)
                os.system("clear")
                bucket.append(select)  # 입력한 책 제목을 장바구니에 추가
                print('=====================₍ ᐢ. ̫ .ᐢ ₎==================')
                print(f"장바구니 리스트 {bucket}\n")
                print('===============================================')

                runprint = False
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

    rent_book()

    # elif runprint:
    # print("입력하신 책 정보가 없습니다.")


def rent_book():
    global book
    global bucket
    select2 = ''
    delete2 = ''

    while (1):
        print_taken = []
        if not bucket == []:
            print(f"내 장바구니 목록 ₍ ᐢ. ̫ .ᐢ ₎ . . {bucket}\n")

        print('=' * 55)
        print('1.이전 화면으로 2.장바구니 삭제 3.대여 4.메인으로 5.반납\n')
        select2 = input()

        if select2 == '1':
            print('장바구니 화면으로 돌아갑니다')
            bucket_book()

        if select2 == '2':
            while not (delete2 == 'q' or delete2 == 'Q'):
                delete2 = input('삭제할 책 이름을 입력해주세요 종료하려면 q\n')
                for i in range(len(bucket)):

                    if delete2 == bucket[i]:
                        os.system("clear")
                        print(". . . 삭제중")
                        time.sleep(2)
                        print(f"{bucket[i]} 장바구니에서 삭제 했습니다.")
                        time.sleep(1)
                        os.system("clear")

                        del bucket[i]

                        if not bucket == []:
                            print(bucket)
                        break
                    else:
                        print("입력하신 책 정보가 없습니다.")

                if delete2 == 'q' or delete2 == 'Q':
                    print("종료합니다")

        if select2 == '3':
            print("장바구니  . . .대여중")
            time.sleep(2)
            if not bucket:
                print('장바구니에 아무것도 없습니다')
                time.sleep(1)
                os.system("clear")
            for i in range(5):
                for j in range(len(bucket)):
                    for k in range(len(user_list)):
                        if bucket[j] == book[i][0] and bucket[j] != user_list[k]:
                            # 무조건 대여중으로 바뀌는 실행문보다 위에있어야함
                            user_list.append(book[i])
                            book[i] = ["대여중 {0}".format(bucket[
                                j])]  # "선택한 제목 이름 대여중"으로 책리스트에 추가
                            os.system("clear")
                            print(f'{bucket}대여되었습니다')
                            bucket = []  # 대여 하고나면 장바구니 비우기
                            time.sleep(1)
                            os.system("clear")

        if select2 == '4':
            main()
        if select2 == '5':
            return_book()


def return_book():
    global book
    global user_list
    turnback = ''
    turnname = ''
    turnnum = ''

    print('    반납 방법을 선택해주세요')
    print('1.도서명으로 반납  2.도서 번호로 반납')
    turnback = input('\n')

    if turnback == '1':
        turnname = input('반납할 책 이름을 입력해주세요\n')
        for i in range(len(user_list)):
            if turnname == user_list[i][0]:  # 반납할 책 이름이 유저 대여 리스트에 있으면
                book.append(user_list[i])
                returninfo.append(user_list[i])  # 반납한 책 리스트에 추가
                del user_list[i]
                for j in range(len(book)):
                    booksplit = book[j][0].split(' ')
                    if (booksplit[0] == '대여중' and turnname == booksplit[1]):
                        del book[j]
                        os.system("clear")
                        time.sleep(2)
                        print(f'{turnname} 반납 되었습니다 ᴖ-ᴖ')
                        break
                break

    if turnback == '2':
        turnnum = input('반납할 책 번호를 입력해주세요')
        for i in range(len(user_list)):
            if turnnum == user_list[i][2]:
                splitname = user_list[i][0]
                book.append(user_list[i])
                returninfo.append(user_list[i])  # 반납한 책 리스트에 추가
                del user_list[i]
                for j in range(5):
                    booksplit = book[j][0].split(' ')
                    if (booksplit[0] == '대여중' and splitname == booksplit[1]):
                        del book[j]
                        os.system("clear")
                        time.sleep(2)
                        print(f'{splitname} 반납 되었습니다 ᴖ-ᴖ')
                        break
                break


def SearchBar():  # 조회
    while 1:

        find = input('-' * 3 + '도서 자료를 입력해 주세요' + '-' * 3 +
                     '\n' + '(도서 / 저자 / 고유 번호)(종료:나가기): ')
        for i in range(len(book)):
            for j in range(len(book[i])):
                if find in book[i][j].split(' '):
                    print(
                        '-' * 20 + '\n' + '도  서 : ' + f'{book[i][0]}' + '\n' + '저  자 : ' + f'{book[i][1]}' + '\n' + '고유번호 : ' + f'{book[i][2]}' + '\n' + '-' * 20)
                elif find == '나가기':
                    print('검색을 종료 합니다')
                    time.sleep(1)
                    os.system("clear")
                    return


def Recommend():
    c.execute("SELECT bookname FROM booklist ORDER by RANDOM() LIMIT 3")
    print('=' * 20 + '추천 도서' + '=' * 20)
    print(*c.fetchall(), sep='\n')
    print('=' * 49)


def Donation():
    c.execute("SELECT * FROM booklist")
    allBook = c.fetchall()

    booklen = len(allBook)  # 총 길이 값
    donate = input("'기증' 하시겠습니까?(Y/n)")
    if donate == 'Y' or donate == 'y':
        bookname = input('도서 명: ')
        writer = input('저자: ')
        c.execute('INSERT INTO booklist values(?, ?, ?)',
                  (booklen, bookname, writer))
    elif donate == 'N' or donate == 'n':
        print('기증을 취소합니다')
        return
    else:
        print('다시 입력하세요')
        return Donation()

    # 마지막 줄 확인(삭제예정)-
    c.execute(f'SELECT * FROM booklist LIMIT {booklen}, {booklen}')
    print(c.fetchall())  # 추가 확인 확인(지울 예정)
    #conn.commit()


def make_id(regist_user):  # 아이디생성 함수

    while 1:
        global uid
        uid = str(input('아이디를 입력하세요: '))
        if uid in regist_user:  # 아이디 중복 확인
            print('중복됨 ㅇㅇ')
            ex = input('메인 화면으로 이동? ㅋㅋ (y/n): ')
            if ex == 'y' or ex == 'Y':
                return 0
            else:
                continue
        else:  # 아이디 중복 아닐 시
            regist_id.append(uid)  # append로 리스트에 추가
            break

    while 1:
        global pwd
        pwd = str(input('비밀번호를 입력하세요: '))
        regist_id.append(pwd)  # 조건 만족 시 추가 (생성)
        break

    while 1:
        global name
        name = str(input('이름을 입력하세요: '))
        regist_id.append(name)  # 조건 만족 시 추가 (생성)
        break

    while 1:
        global num
        num = str(input('번호를 입력하세요: '))
        regist_id.append(num)  # 조건 만족 시 추가 (생성)
        break
    c.execute('INSERT INTO userlist VALUES (?,?,?,?)', (uid, pwd, name, num))
    return regist_id


def change_password(pwd):  # 비밀번호 바꾸기
    global UserID
    while 1:
        pw = str(input('새로운 비번 입력:'))
        if pw == pwd:  # 바꿀 비번이 기본과 똑같을때
            print(f'기존의 비밀번호 입니다.!')
            continue
        else:
            n_pwd = pw
            break
    c.execute("update userlist set pwd = ? where id = ?",(n_pwd, UserID))
    print('수정완료')
    time.sleep(1)
    os.system('clear')
    return n_pwd

def change_name(name):
    global UserID
    while 1:
        new_name = str(input('변경할 이름입력:'))
        if new_name == name:
            print(f'기존과 동일한 이름 입니다.!')
            continue
        else:
            n_name = new_name
            break
    c.execute("update userlist set name = ? where id = ?",(n_name, UserID))
    print('수정완료')
    time.sleep(1)
    os.system('clear')
    return n_name


def change_num(num):
    global UserID
    while 1:
        new_num = str(input('변경할 번호입력:'))
        if new_num == num:
            print(f'기존과 동일한 번호 입니다.!')
            continue
        else:
            n_num = new_num
            break
    c.execute("update userlist set num = ? where id = ?", (n_num, UserID))
    print('수정완료')
    time.sleep(1)
    os.system('clear')
    return n_num


def main():
    global returninfo
    menu_select = ''
    slt = ''
    os.system("clear")
    while (1):
        time.sleep(1)
        os.system("clear")

        Recommend()  # 추천 도서 함수

        print('1.조회 2.대여 3.반납 4.기증 5.나의정보')
        menu_select = input()

        if (menu_select == '1'):
            SearchBar()  # 도서 검색 함수
        if (menu_select == '2'):
            bucket_book()  # 대여/장바구니 함수
        if (menu_select == '3'):
            return_book()  # 반납 함수
        if (menu_select == '4'):
            Donation()  # 기증 함수
        if (menu_select == '5'):
            while (1):
                os.system("clear")
                time.sleep(1)
                print('---------ଘʕ੭·ㅅ·ʔ੭ 내 정보 ଘʕ੭·ㅅ·ʔ੭---------')

                print('▶ 대여중인 도서 리스트')
                if not user_list == []:
                    print(user_list)

                print('=' * 30)
                print('▶ 대여후 반납한 도서 리스트')
                if not returninfo == []:
                    print(returninfo)

                print('▶ 미납중인 도서 리스트')
                if not user_list == []:
                    print(user_list)
                print('=' * 30)

                print('1.내 정보 변경')
                print('2.연체 정보 조회하기')
                print('-----------------------------------------')
                slt = input()
                if slt == '1':  # 내 정보 변경
                    regist_user = {}  # regist_user 딕셔너리 (만든 아이디 저장)
                    sw = 1
                    while sw:
                        c.execute("SELECT id,pwd FROM userlist")  # 로그인할때 필요한 id,pwd읽기
                        db_user = c.fetchall()  # 동일함
                        print('1)비밀번호 변경 2)이름 변경 3)번호 변경 4)나가기')
                        choice = int(input('선택해주세요:'))
                        if (choice == 1):
                            uid = str(input('아이디를 입력해주세요:'))
                            c.execute("SELECT id FROM userlist")
                            db_id = c.fetchall()
                            for search in db_id:
                                if uid in search:
                                    new_pwd = change_password(pwd)
                                    print('비밀번호 변경 완료\n')
                                else:
                                    continue

                        elif (choice == 2):
                            uid = str(input('아이디를 입력해주세요:'))
                            c.execute("SELECT id FROM userlist")
                            db_id = c.fetchall()
                            for search in db_id:
                                if uid in search:
                                    new_name = change_name(name)
                                    print('이름 변경 완료\n')
                                else:
                                    continue
                        elif (choice == 3):
                            uid = str(input('아이디를 입력해주세요:'))
                            c.execute("SELECT id FROM userlist")
                            db_id = c.fetchall()
                            for search in db_id:
                                if uid in search:
                                    new_num = change_num(num)
                                    print('번호 변경 완료\n')
                                else:
                                    continue
                        elif (choice == 4):
                            break
                        else:
                            print('1~4 중에 골라주세요')
                            continue
                if slt == '2':
                    print('연체 정보 없음')

                if slt == 'q' or 'ㅂ':
                    break


def main2():
    global UserID
    regist_user = {}  # regist_user 딕셔너리 (만든 아이디 저장)
    sw = 1  # while문 1 or 0 조건을 위해 선언
    while sw:
        c.execute("SELECT id,pwd FROM userlist")  # 로그인할때 필요한 id,pwd읽기
        db_user = c.fetchall()  # 동일함
        print('-' * 30)
        print('1. 아이디 생성')
        print('2. 아이디 & 비밀번호 찾기')
        print('3. 아이디 목록 ')
        print('4. 로그인 ')
        print('5. 종료')
        print('-' * 30)
        select_no = int(input('번호 선택(1~5): '))

        if select_no == 1:  # 아이디생성
            id_result = make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print('ID 생성 완료!')
                time.sleep(1)
                os.system('clear')

        elif select_no == 2:  # ID/PW 찾기
            global name
            name = input('회원가입한 ID를 입력하세요: ')
            for search in db_user:
                if name in search:
                    print(search)
                    time.sleep(2)
                    break
                else:
                    # print('등록된 ID가 아닙니다.\n')
                    time.sleep(1)
                    continue

        elif select_no == 3:  # 아이디 목록 확인
            for i in db_user:
                print(i)
            time.sleep(2)
            os.system('clear')

        elif select_no == 4:  # 로그인
            id_input = input('ID 입력:')
            pw_input = input('PW 입력:')
            for search in db_user:
                if id_input == search[0] and pw_input == search[1]:
                    print('로그인 성공')
                    UserID=id_input
                    time.sleep(2)
                    main()
            else:
                print('로그인 실패')
                continue
        elif select_no == 5:  # 종료
            sw = 0
        else:  # 예외처리
            print('잘못입력하셨습니다. 1~5 중에 골라주세요')
            time.sleep(1)
            os.system('clear')
            continue


main2()
c.close()
