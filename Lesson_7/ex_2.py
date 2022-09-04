# 2) Реализуйте свой аналог генераторной функции range(). Да, вы теперь
# знаете, что это - генератор.

def my_range(*args) -> int:
    match len(args):
        case 1:
            start, stop, step = 0, args[0], 1
        case 2:
            start, stop, step = args[0], args[1], 1
        case 3:
            start, stop, step = args[0], args[1], args[2]
        case _:
            raise TypeError
    while start < stop:
        yield start
        start += step


a = 1
b = 7
c = 1

for i in my_range(2, 5, 1):
    print(i)

