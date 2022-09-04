from __future__ import annotations

import product_module
import customer_module


class Cart:

    def __init__(self, customer: customer_module.Customer = None):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def add_product(self, product: product_module.Product, quantity=1):
        if product in self.__products:
            index = self.__products.index(product)
            self.__quantities[index] += quantity
        else:
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        res = 0
        for index, item in enumerate(self.__products):
            res += item.price * self.__quantities[index]
        return res

    def __str__(self):
        res = f'{self.customer}\n'

        for index, item in enumerate(self.__products):
            res += f'\t{item} x {self.__quantities[index]} = {item.price * self.__quantities[index]} грн.\n'

        res += f'Total price: {self.total()} грн.'
        return res

    def __len__(self):
        return len(self.__products)

    def __getitem__(self, item: int | slice):
        if isinstance(item, int) or isinstance(item, slice):
            products = self.__products[item]
            quantity = self.__quantities[item]
            result = []
            for i, item in enumerate(products):
                result.append((item, quantity[i]))
            return result

        raise TypeError("Param 'item' must be an integer | slice ")

    def __iter__(self):
        return CardIteration(self.__products)


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
