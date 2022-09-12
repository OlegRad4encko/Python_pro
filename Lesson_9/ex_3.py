# 3) Предположим, в классе определен метод __str__, который возвращает
# строку на основании класса. Создайте такой декоратор для этого метода,
# чтобы полученная строка сохранялась в текстовый файл, имя которого
# совпадает с именем класса, метод которого вы декорировали.


def decorator(method):
    def inner(*args, **kwargs):
        result = method(*args)
        with(open("User.txt", 'a') as f):
            # Не сообразил, как лучше будет сделать "имя файла = имя класса"
            f.write(result)
        return result

    return inner


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @decorator
    def __str__(self):
        return f'{self.name} {self.surname}, {self.age} years old\n'


p1 = User("Oleh", "Radchenko", 23)
print(p1)
print(p1)
