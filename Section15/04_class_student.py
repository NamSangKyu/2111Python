'''
    학생 클래스는 학번, 이름, 학과, 평점을 저장하고 있음
    학생 클래스가 가지고 있는 메서드는
    setting_data를 이용해서 학번, 이름, 학과, 평점을 저장을 하고
    print_student_info를 이용해서 student 객체가 가지고 있는 내용을 출력
'''
class Student:
    def setting_data(self,no, name, major, score):
        self.no = no
        self.name = name
        self.major = major
        self.score = score

    def print_student_info(self):
        print(f'{self.no}\t{self.name}\t{self.major}\t{self.score}')

student1 = Student()
student1.setting_data('20211111','홍길동','컴퓨터공학과',3.45)
student1.print_student_info()