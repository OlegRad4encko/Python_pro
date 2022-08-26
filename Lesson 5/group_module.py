from __future__ import annotations

import env
import userErrors
import student_module


class Group:
    def __init__(self, group_name: str, group_number: str) -> None:
        self.group_name = group_name
        self.group_number = group_number
        self.students = []

    def add_student(self, student: student_module.Student) -> int:
        if len(self.students) == env.MAX_STUDENTS_IN_GROUP:
            raise userErrors.MaxStudentError(env.MAX_STUDENTS_IN_GROUP)
        if student in self.students:
            raise userErrors.StudentIsAlreadyInTheGroupError(student,
                                                             f'{self.group_name}{self.group_number}')
        self.students.append(student)

    def delete_student(self, student: student_module.Student) -> int:
        if student in self.students:
            self.students.pop(self.students.index(student))
            return 1
        raise userErrors.DeleteStudentFromTheGroupError(student, f'{self.group_name}{self.group_number}')

    def search_student_by_surname(self, surname: str) -> int | student_module.Student:
        for item in self.students:
            if item.surname.lower() == surname.lower():
                return item
        raise userErrors.SearchStudentBySurnameError(surname, f'{self.group_name}{self.group_number}')

    def __str__(self) -> str:
        result = f'Group: {self.group_name}{self.group_number}\n'
        if not self.students:
            return result + f'Empty\n\n'
        for index, item in enumerate(self.students):
            result += f'{self.students[index]}\n'
        return result
