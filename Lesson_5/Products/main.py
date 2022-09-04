import random

import user_except
import product_module
import customer_module
import card_module


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
        products_list.append(product_module.Product(products[elem]["product_name"], products[elem]["product_price"]))
    except (ValueError, user_except.UserExcept) as err:
        print(f'Opps:\n {err}')

customer_1 = customer_module.Customer('Ivan', 'Ivanov', '123456789')
customer_2 = customer_module.Customer('Ivan', 'Petrov', '223456789')

order_1 = card_module.Cart(customer_1)
order_2 = card_module.Cart(customer_2)

for elem in range(len(products_list)):
    order_1.add_product(products_list[elem], random.randint(1, 5))

for elem in range(len(products_list)):
    order_2.add_product(products_list[elem], random.randint(1, 5))

print(order_2)
print(order_1.total())
