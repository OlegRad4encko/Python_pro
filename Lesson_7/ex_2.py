# 2) Реализуйте свой аналог генераторной функции range(). Да, вы теперь
# знаете, что это - генератор.

def my_range(*args) -> int:
    start = 0
    stop = 0
    step = 1
    match len(args):
        case 1:
            stop = args[0]
        case 2:
            start = args[0]
            stop = args[1]
        case 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        case _:
            raise StopIteration
    while start < stop:
        yield start
        start += step


a = 1
b = 7
c = 1

for i in my_range(b):
    print(i)

