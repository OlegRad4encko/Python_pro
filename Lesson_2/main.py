from __future__ import annotations
import env

import random


def random_record_book_number() -> int:
    return random.randint(100000000, 999999999)


class MaxStudentError(Exception):

    def __init__(self, gr_max_student: int):
        super().__init__()
        self.gr_max_student = gr_max_student

    def __str__(self) -> str:
        return f' В группе было {self.gr_max_student} мест.'


class StudentIsAlreadyInTheGroupError(Exception):

    def __init__(self, student: Student, gr_f_name: str):
        super().__init__()
        self.student = student
        self.gr_f_name = gr_f_name

    def __str__(self) -> str:
        return f'Студент \n{self.student} --- уже находится в этой ({self.gr_f_name}) группе\n\n'


class DeleteStudentFromTheGroupError(Exception):

    def __init__(self, student: Student, gr_f_name: str):
        super().__init__()
        self.student = student
        self.gr_f_name = gr_f_name

    def __str__(self) -> str:
        rez = f'Студента \n{self.student} --- нет в {self.gr_f_name} группе.'
        rez += f' НЕЛЬЗЯ ОТЧИСЛИТЬ\n\n'
        return rez


class SearchStudentBySurnameError(Exception):
    def __init__(self, surname: str, gr_f_name: str):
        super().__init__()
        self.surname = surname
        self.gr_f_name = gr_f_name

    def __str__(self) -> str:
        return f'Студент c фамилией \n({self.surname}) не найден в группе {self.gr_f_name}.'


class Human:
    def __init__(self, name: str,
                 surname: str,
                 birth_date: str) -> None:
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __str__(self) -> str:
        return f'{self.surname} {self.name[0]} [{self.birth_date}]'


class Student(Human):
    def __init__(self,
                 name: str,
                 surname: str,
                 birth_date: str,
                 start_of_studies: str,
                 end_of_studies: str) -> None:
        super().__init__(name, surname, birth_date)
        self.record_book_number = random_record_book_number()
        self.start_of_studies = start_of_studies
        self.end_of_studies = end_of_studies

    def __str__(self) -> str:
        result = f'{self.surname} {self.name[0]}.\t'
        result += f'[{self.start_of_studies}-{self.end_of_studies}] \t RBM: {self.record_book_number}'
        return result


class Group:
    def __init__(self, group_name: str, group_number: str) -> None:
        self.group_name = group_name
        self.group_number = group_number
        self.students = []

    def add_student(self, student: Student) -> int:
        if len(self.students) == env.MAX_STUDENTS_IN_GROUP:
            raise MaxStudentError(env.MAX_STUDENTS_IN_GROUP)
        if student in self.students:
            raise StudentIsAlreadyInTheGroupError(student,
                                                  f'{self.group_name}{self.group_number}')
        self.students.append(student)

    def delete_student(self, student: Student) -> int:
        if student in self.students:
            self.students.pop(self.students.index(student))
            return 1
        raise DeleteStudentFromTheGroupError(student, f'{self.group_name}{self.group_number}')

    def search_student_by_surname(self, surname: str) -> int | Student:
        for item in self.students:
            if item.surname.lower() == surname.lower():
                return item
        raise SearchStudentBySurnameError(surname, f'{self.group_name}{self.group_number}')

    def __str__(self) -> str:
        result = f'Group: {self.group_name}{self.group_number}\n'
        if not self.students:
            return result + f'Empty\n\n'
        for index, item in enumerate(self.students):
            result += f'{self.students[index]}\n'
        return result


group = Group("KB-", "81-0")

students = []
x1 = Student("Oleh", "Radchenko", "11.07.2000", "01.09.2020", "30.07.2022")
x2 = Student("Sergei", "Shargin", "12.07.2001", "01.09.2020", "30.07.2022")
x3 = Student("Alina", "Grishenko", "13.07.2000", "01.09.2020", "30.07.2022")
x4 = Student("Nastya", "Sahno", "14.07.2001", "01.09.2020", "30.07.2022")
x5 = Student("Vika", "Ponamarenko", "15.07.2001", "01.09.2020", "30.07.2022")
x6 = Student("Dima", "Raiko", "16.07.2001", "01.09.2020", "30.07.2022")
x7 = Student("Katya", "Raiko", "17.07.2001", "01.09.2020", "30.07.2022")
x8 = Student("Vlad", "Grishchenko", "18.07.2000", "01.09.2020", "30.07.2022")
x9 = Student("Andrey", "Kozachek", "19.07.2001", "01.09.2020", "30.07.2022")
x10 = Student("Anton", "Petlenko", "20.07.2000", "01.09.2020", "30.07.2022")
x11 = Student("Max", "Petlenko", "20.07.2000", "01.09.2020", "30.07.2022")

print(group)

try:
    group.add_student(x1)
    group.add_student(x2)
    group.add_student(x3)
    group.add_student(x4)
    group.add_student(x5)
    group.add_student(x6)
    group.add_student(x7)
    group.add_student(x8)
    group.add_student(x9)
    group.add_student(x1)
    group.add_student(x10)
    group.add_student(x11)
except (MaxStudentError, StudentIsAlreadyInTheGroupError) as err:
    print(err)

print(group)

try:
    group.delete_student(x10)
except DeleteStudentFromTheGroupError as err:
    print(err)

print(group)

try:
    print(group.search_student_by_surname("Radchenko"))
except () as err:
    print(err)
