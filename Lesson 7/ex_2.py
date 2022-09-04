# 2) Реализуйте свой аналог генераторной функции range(). Да, вы теперь
# знаете, что это - генератор.

def my_range(start: int, stop=0, inc=1) -> int:
    if stop == 0:
        stop = start, start = stop
    index = start
    while index < stop:
        yield index
        index += inc

# a = 1
# b = 7
# c = 2
#
# for i in my_range(a, b, c):
#     print(i)
#
# print("\n")
#
# for i in range(a, b, c):
#     print(i)
