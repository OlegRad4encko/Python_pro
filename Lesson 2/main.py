from __future__ import annotations

import random


def random_record_book_number() -> int:
    return random.randint(100000000, 999999999)


class Human:
    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __str__(self):
        return f'{self.surname} {self.name[0]} [{self.birth_date}]'


class Student(Human):
    def __init__(self, name, surname, birth_date, start_of_studies, end_of_studies):
        super().__init__(name, surname, birth_date)
        self.record_book_number = random_record_book_number()
        self.start_of_studies = start_of_studies
        self.end_of_studies = end_of_studies


    def __str__(self):
        result = f'{self.surname} {self.name[0]}.\t'
        result += f'[{self.start_of_studies}-{self.end_of_studies}] \t RBM: {self.record_book_number}'
        return result


class Group(Student):
    def __init__(self, group_name, group_number):
        self.group_name = group_name
        self.group_number = group_number
        self.students = []

    def add_student(self, student):
        if len(self.students) == 10:
            print("Достигнут лимит студентов в группе, сформируйте еще одну группу.\n")
            return 0
        if student in self.students:
            print("Такой студент уже есть в этой группе.\n")
            return 0
        self.students.append(student)
        return 0

    def delete_student(self, student):
        print(f'Студент ({student}) отчислен \n')
        self.students.pop(self.students.index(student))
        return 0

    def search_student_by_surname(self, surname):
        result = f'Студент(ы) найден(ы):\n'
        for index, item in enumerate(self.students):
            if str(self.students[index]).find(surname) == 0:
                result += f'{self.students[index]}\n'
        print(result)
        return 0

    def __str__(self):
        result = f'Group: {self.group_name}{self.group_number}\n'
        for index, item in enumerate(self.students):
            result += f'{self.students[index]}\n'
        return result


group = Group("KB-", "81-0")

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

group.add_student(x1)
group.add_student(x2)
group.add_student(x3)
group.add_student(x4)
group.add_student(x5)

print(group)

group.add_student(x6)
group.add_student(x7)
group.add_student(x8)
group.add_student(x9)
group.add_student(x1)

print(group)

group.add_student(x10)
group.add_student(x11)

print(group)

group.delete_student(x10)

print(group)

group.search_student_by_surname("Raiko")
