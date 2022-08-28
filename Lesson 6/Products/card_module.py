from __future__ import annotations

import product_module
import customer_module


class Cart:

    def __init__(self, customer: customer_module.Customer = None):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: product_module.Product, quantity: int | float):
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

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item: int | slice):
        if isinstance(item, int):
            return self.products[item]
        if isinstance(item, slice):
            return self.products[item]
        raise TypeError("Param 'item' must be a integer | slice ")

    def __iter__(self):
        return CardIteration(self.products)


class CardIteration:
    def __init__(self, wrapper: list):
        self.wrapper = wrapper
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.wrapper):
            self.index += 1
            return self.wrapper[self.index - 1]
        raise StopIteration
