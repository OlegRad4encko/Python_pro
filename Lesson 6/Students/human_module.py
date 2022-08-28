class Human:
    def __init__(self, name: str,
                 surname: str,
                 birth_date: str) -> None:
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __str__(self) -> str:
        return f'{self.surname} {self.name[0]} [{self.birth_date}]'