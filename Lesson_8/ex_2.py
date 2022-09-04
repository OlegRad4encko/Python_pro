# Используя функцию замыкания реализуйте такой прием программирования
# как Мемоизация - https://en.wikipedia.org/wiki/Memoization
# Используйте полученный механизм для ускорения функции рекурсивного
# вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
# просто рекурсивным подходом.
import timeit

t1 = """
def fib(n):
    n += 1
    memory_first = [0, ]
    memory_second = [1, ]
    memory_value = [1, ]
    first_n = 0
    second_n = 1

    def get_next(k):
        nonlocal second_n
        nonlocal first_n

        if k <= len(memory_value) - 1:
            return memory_value[0:k]
        if first_n < memory_first[-1] and second_n < memory_second[-1]:
            first_n, second_n = memory_first[-1], memory_second[-1]
        next_n = second_n + first_n
        first_n = second_n
        second_n = next_n
        memory_value.append(next_n)
        memory_first.append(second_n)
        memory_second.append(next_n)
        return next_n

    return get_next


x = fib(20)
for i in range(20):
    tmp = x(10)
    if isinstance(tmp, list):
        print(tmp)
        break

for i in range(10):
    tmp = x(8)
    if isinstance(tmp, list):
        print(tmp)
        break

"""

t2 = """
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(20))

print(fibonacci(9))
"""

print(timeit.timeit(t1, number=2))
print(timeit.timeit(t2, number=2))

