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
            raise TypeError()
    if step == 0:
        raise ValueError()
    if start > stop and step > 0:
        raise ValueError()
    if stop > start and step < 0:
        while stop > start:
            yield stop
            stop += step
    else:
        while start < stop:
            yield start
            start += step




for i in my_range(1, 5, -1):
    print(i)

