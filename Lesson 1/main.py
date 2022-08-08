import random


class Product:
    def __init__(self, product_data):
        self.price = product_data["price"]
        self.description = product_data["description"]
        self.height = product_data["height"]
        self.width = product_data["width"]
        self.long = product_data["long"]

    def __str__(self):
        result_string = f'Product name: {self.description}\n'
        result_string += f' * how it cost: {self.price}\n'
        result_string += f' * size of product: {self.long}x{self.width}x{self.height}\n'
        return result_string

    def get_product_data(self):
        return {
            "description": self.description,
            "price": self.price,
            "size_of_product": f'{self.long}x{self.width}x{self.height}',
        }


class Customer:
    def __init__(self, customer_data):
        self.name = customer_data["name"]
        self.surname = customer_data["surname"]
        self.address = customer_data["address"]
        self.phone_number = customer_data["phone_number"]

    def __str__(self):
        result_string = f'Customer profile:\n'
        result_string += f' * name: {self.name}\n'
        result_string += f' * surname: {self.surname}\n'
        result_string += f' * address: {self.address}\n'
        result_string += f' * phone number: {self.phone_number}\n'
        return result_string

    def get_customer_data(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "address": self.address,
            "phone_number": self.phone_number
        }


class Order:

    def __init__(self, customer):
        self.owner = customer
        self.products_list = []
        self.product_name_list = []
        self.product_price_list = []
        self.product_size_list = []

    def add_product(self, product):
        self.product_name_list.append(product["description"])
        self.product_price_list.append(product["price"])
        self.product_size_list.append(product["size_of_product"])

    def get_final_price(self):
        final_price = 0
        for i in range(len(self.product_price_list)):
            final_price += self.product_price_list[i]
        return final_price

    def __str__(self):
        tmp = f'Customer: {self.owner["surname"]} {self.owner["name"][0]}.\n'
        tmp += f'Customer address: {self.owner["address"]}\n'
        tmp += f'Customer phone number: {self.owner["phone_number"]}\n'
        tmp += "=============== Order list ===============\n"
        for i in range(len(self.product_name_list)):
            tmp += f'Product name: {self.product_name_list[i]},\t'
            tmp += f'Size: {self.product_size_list[i]},\t'
            tmp += f'Price: {self.product_price_list[i]}\n'
        tmp += f'===================== Full cost of the order: {self.get_final_price()}\n'
        return tmp

    def get_count(self):
        return len(self.products_list)


products = [
    {
        "price": 150,
        "description": "FACE MASK",
        "height": 3,
        "width": 30,
        "long": 30,
    },
    {
        "price": 300,
        "description": "Education Atlas",
        "height": 0,
        "width": 28,
        "long": 18,
    },
    {
        "price": 450,
        "description": "Cup",
        "height": 18,
        "width": 18,
        "long": 18,
    }
]
customers = [
    {
        "name": "Oleh",
        "surname": "Radchenko",
        "address": "m. Sumy",
        "phone_number": "380000000000"
    },
    {
        "name": "Kate",
        "surname": "Medvedeva",
        "address": "m. Harkiv",
        "phone_number": "380000000000"
    },
    {
        "name": "Dmitry",
        "surname": "Raiko",
        "address": "m. Kyiv",
        "phone_number": "380000000000"
    },
    {
        "name": "Karina",
        "surname": "Ovramenko",
        "address": "m. Sevastopol",
        "phone_number": "380000000000"
    },
]

products_list = []
customers_list = []
order_list = []
for element in range(len(products)):
    products_list.append(Product(products[element]))
for element in range(len(customers)):
    customers_list.append(Customer(customers[element]))

print()

for element in range(random.randint(5, 10)):
    order_list.append(Order(customers_list[random.randint(0, len(customers_list) - 1)].get_customer_data()))

for element in range(len(order_list)):
    for j in range(0, 3):
        order_list[element].add_product(products_list[random.randint(0, len(products_list) - 1)].get_product_data())

for element in order_list:
    print(element)
