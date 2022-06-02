import sqlite3
import random

libraryBook = sqlite3.connect("lib_project.db")

with libraryBook:
    cur = libraryBook.cursor()
    bookAll = "SELECT * FROM booklist"
    cur.execute(bookAll)
    allBook = cur.fetchall()

def Recommend():
    cur.execute("SELECT bookname FROM booklist ORDER by RANDOM() LIMIT 3")
    print('=' * 20 + '추천 도서' + '=' * 20)
    print(*cur.fetchall(), sep='\n')
    print('=' * 49)

Recommend()

def Donation():
    booklen = len(allBook)  # 총 길이 값
    donate = input("'기증' 하시겠습니까?(Y/n)")
    if donate == 'Y' or donate == 'y':
        bookname = input('도서 명: ')
        writer = input('저자: ')
        cur.execute('INSERT INTO booklist values(?, ?, ?)', (booklen, bookname, writer))
    elif donate == 'N' or donate == 'n':
        print('기증을 취소합니다')
        return
    else:
        print('다시 입력하세요')
        return Donation()

    cur.execute(f'SELECT * FROM booklist LIMIT {booklen}, {booklen}')  # 마지막 줄 확인(삭제예정)-
    print(cur.fetchall())  # 추가 확인 확인(지울 예정)
    libraryBook.commit()

Donation()
