# 2) Создайте декоратор класса с параметром. Параметром должна быть
# строка, которая должна дописываться (слева) к результату работы метода
# __str__.

def parent(text=None):
    def decorator(method):
        def inner(*args, **kwargs):
            return f'{text} {method(*args)}'

        return inner
    return decorator


class A:
    def __init__(self, my_str: str):
        self.my_str = my_str

    @parent("Hello")
    def __str__(self):
        return self.my_str


e1 = A("Oleh")
print(e1)


