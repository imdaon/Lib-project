class bookInfo:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.status = kwargs['status']
        self.bookname = kwargs['bookname']
        self.writer = kwargs['writer']

library = []
library.append(bookInfo(**{'id': 1, 'status': '대출 불가', 'bookname': '천사와 악마', 'writer': '댄 브라운'}))
library.append(bookInfo(**{'id': 2, 'status': '대출 가능', 'bookname': '다잉아이', 'writer': '히가시노 게이고'}))
library.append(bookInfo(**{'id': 3, 'status': '대출 가능', 'bookname': '검은모레', 'writer': '구소은'}))

find = input("찾으려는 '도서 명' 또는 '저자' 검색: ")

for book in library:
    if book.writer == find: #저자 검색
        print('\n'+'-'*20+'\n'+'현 상태: '+book.status+'\n도서 명:'+book.bookname+'\n저 자: '+book.writer+'\n'+'-'*20)
    if book.bookname == find: #도서 명 검색
        print('\n'+'-'*20+'\n'+'현 상태: '+book.status+'\n도서 명:'+book.bookname+'\n저 자: '+book.writer+'\n'+'-'*20)
