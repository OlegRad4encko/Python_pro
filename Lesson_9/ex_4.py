# 4) Создайте декоратор с параметрами для проведения хронометража работы
# той или иной функции. Параметрами должны выступать то, сколько раз нужно
# запустить декорируемую функцию и в какой файл сохранить результаты
# хронометража. Цель - провести хронометраж декорируемой функции.

import time


def parent(count_repeats=1, output_file="tmp_file.txt"):
    def my_decorator(f):
        def inner(*args):
            start = time.time_ns()
            for i in range(count_repeats):
                result = f(*args)
            stop = time.time_ns()
            with(open(output_file, 'a') as file):
                file.write(f'{f.__name__}, {start}-{stop}\n')
            return result

        return inner

    return my_decorator


@parent(2, "hello.txt")
def my_func(tmp):
    return 1 + tmp


print(my_func(1))