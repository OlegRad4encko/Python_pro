from __future__ import annotations


import user_except


class Product:
    def __init__(self, title: str, price: int | float):
        self.title = title
        if price <= 0:
            raise user_except.UserExcept()
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} грн.'
