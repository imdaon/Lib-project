from unicodedata import name


class Student:
    def __init__(self, name, korean, math, En, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.En = En
        self.science = science  # 클래스
    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}".format(self.name,self.korean,self.math,self.En,self.science)


class score(Student):
    def get_sum(self):
        return self.korean + self.En + self.math + self.science

    def get_avr(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avr())


students = [
    score("박승렬", 87, 98, 88, 95),
    score("정정빈", 90, 99, 80, 90),
    score("방은혁", 100, 90, 80, 70),
    score("성민식", 70, 80, 90, 100),
    score("이의현", 77, 88, 99, 95),
    score("양현동", 88, 70, 88, 100),
]  # 리스트
print("이름\t", "총점", "평균")
for students in students:
    print(students.to_string())

"""a=Student("박승렬",87,98,88,95) #이건 클래스를 쓰기위한 객체 선언
print(a.name) #객체를 선언후 해당 self에 맞춰 값을 입력한 후 출력하는거임
print(a.En)
print(a.korean)
print(a.math)
print(a.science)
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(students[0].name)  #  이건 리스트에 접근해서 출력하는것"""
