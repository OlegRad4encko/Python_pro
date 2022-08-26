import student_module


class MaxStudentError(Exception):

    def __init__(self, gr_max_student: int):
        super().__init__()
        self.gr_max_student = gr_max_student

    def __str__(self) -> str:
        return f' В группе было {self.gr_max_student} мест.'


class StudentIsAlreadyInTheGroupError(Exception):

    def __init__(self, student: student_module.Student, gr_f_name: str):
        super().__init__()
        self.student = student
        self.gr_f_name = gr_f_name

    def __str__(self) -> str:
        return f'Студент \n{self.student} --- уже находится в этой ({self.gr_f_name}) группе\n\n'


class DeleteStudentFromTheGroupError(Exception):

    def __init__(self, student: student_module.Student, gr_f_name: str):
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
