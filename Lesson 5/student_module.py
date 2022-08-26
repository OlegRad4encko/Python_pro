import human_module
import random


def random_record_book_number() -> int:
    return random.randint(100000000, 999999999)


class Student(human_module.Human):
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
