from __future__ import annotations
import env


import userErrors
import student_module
import group_module

group = group_module.Group("KB-", "81-0")

students = []
x1 = student_module.Student("Oleh", "Radchenko", "11.07.2000", "01.09.2020", "30.07.2022")
x2 = student_module.Student("Sergei", "Shargin", "12.07.2001", "01.09.2020", "30.07.2022")
x3 = student_module.Student("Alina", "Grishenko", "13.07.2000", "01.09.2020", "30.07.2022")
x4 = student_module.Student("Nastya", "Sahno", "14.07.2001", "01.09.2020", "30.07.2022")
x5 = student_module.Student("Vika", "Ponamarenko", "15.07.2001", "01.09.2020", "30.07.2022")
x6 = student_module.Student("Dima", "Raiko", "16.07.2001", "01.09.2020", "30.07.2022")
x7 = student_module.Student("Katya", "Raiko", "17.07.2001", "01.09.2020", "30.07.2022")
x8 = student_module.Student("Vlad", "Grishchenko", "18.07.2000", "01.09.2020", "30.07.2022")
x9 = student_module.Student("Andrey", "Kozachek", "19.07.2001", "01.09.2020", "30.07.2022")
x10 = student_module.Student("Anton", "Petlenko", "20.07.2000", "01.09.2020", "30.07.2022")
x11 = student_module.Student("Max", "Petlenko", "20.07.2000", "01.09.2020", "30.07.2022")

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
except (userErrors.MaxStudentError, userErrors.StudentIsAlreadyInTheGroupError) as err:
    print(err)

print(group)

try:
    group.delete_student(x10)
except userErrors.DeleteStudentFromTheGroupError as err:
    print(err)

print(group)

try:
    print(group.search_student_by_surname("Radchenko"))
except () as err:
    print(err)
