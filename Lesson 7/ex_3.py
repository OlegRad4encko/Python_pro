# Напишите функцию-генератор, которая будет возвращать простые числа.
# Верхняя граница этого диапазона должна быть задана параметром этой
# функции.

def prime_numbers(n):
    min = 2
    max = n + 1
    for i in range(min, max):
        for j in range(min, max):
            if i % j == 0:
                break
        if j == i:
            yield i


my_prime_nums = prime_numbers(200)
for item in my_prime_nums:
    print(item)
