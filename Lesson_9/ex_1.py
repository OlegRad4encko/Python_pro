# 1) Создайте декоратор, который будет подсчитывать, сколько раз была
# вызвана декорируемая функция.


class Decorator:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        result = self.func(*args, **kwargs)
        return result


@Decorator
def my_func(my_str: str):
    return f'Hello, {my_str}'


print(my_func("Oleh"))
print(my_func("Oleh"))
print(my_func.counter)
