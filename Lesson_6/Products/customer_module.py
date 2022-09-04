from __future__ import annotations


class Customer:
    def __init__(self, name: str, surname: str, phone: str):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.phone}'
