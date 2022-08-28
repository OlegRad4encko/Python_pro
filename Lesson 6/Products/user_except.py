from __future__ import annotations


class UserExcept(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'Цена продукта должна быть больше 0'
