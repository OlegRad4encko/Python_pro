from __future__ import annotations

import random


class UserExcept(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'Цена продукта должна быть больше 0'


class Product:

    def __init__(self, title: str, price: int | float):
        self.title = title
        if price <= 0:
            raise UserExcept()
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} грн.'


class Customer:

    def __init__(self, name: str, surname: str, phone: str):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.phone}'


class Cart:

    def __init__(self, customer: Customer = None):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total(self):
        res = 0
        for index, item in enumerate(self.products):
            res += item.price * self.quantities[index]
        return res

    def __str__(self):
        res = f'{self.customer}\n'

        for index, item in enumerate(self.products):
            res += f'\t{item} x {self.quantities[index]} = {item.price * self.quantities[index]} грн.\n'

        res += f'Total price: {self.total()} грн.'

        return res


products = [
    {
        "product_name": "banana",
        "product_price": 20
    },
    {
        "product_name": "apple",
        "product_price": 21
    },
    {
        "product_name": "orange",
        "product_price": 0
    }
]

products_list = []

for elem in range(len(products)):
    try:
        products_list.append(Product(products[elem]["product_name"], products[elem]["product_price"]))
    except (ValueError, UserExcept) as err:
        print(f'Opps:\n {err}')

customer_1 = Customer('Ivan', 'Ivanov', '123456789')
customer_2 = Customer('Ivan', 'Petrov', '223456789')

order_1 = Cart(customer_1)
order_2 = Cart(customer_2)

for elem in range(len(products_list)):
    order_1.add_product(products_list[elem], random.randint(1, 5))

for elem in range(len(products_list)):
    order_2.add_product(products_list[elem], random.randint(1, 5))

print(order_2)
print(order_1.total())
